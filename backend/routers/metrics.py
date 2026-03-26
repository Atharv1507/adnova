from fastapi import APIRouter, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional

from services.openai_service import (
    analyze_creative_performance,
    analyze_text_only_performance
)
from services.media_utils import process_uploaded_file, encode_image_to_base64

router = APIRouter(prefix="/api", tags=["Business Metrics"])


def calculate_metrics(
    spend_total: float,
    orders: int,
    cost_price: float,
    selling_price: float,
    days: int
) -> dict:
    """Core business metrics calculation engine."""
    revenue = selling_price * orders
    cogs_total = cost_price * orders
    net_profit = revenue - spend_total - cogs_total
    cpa = spend_total / orders if orders > 0 else 0
    roas = revenue / spend_total if spend_total > 0 else 0
    margin = (selling_price - cost_price) / selling_price if selling_price > 0 else 0
    break_even_roas = 1 / margin if margin > 0 else 0
    roi = (net_profit / spend_total * 100) if spend_total > 0 else 0
    profit_margin_pct = (net_profit / revenue * 100) if revenue > 0 else 0
    spend_per_day = spend_total / days if days > 0 else spend_total

    if roas >= break_even_roas * 1.3:
        verdict = "Strong Performer"
        verdict_color = "green"
    elif roas >= break_even_roas:
        verdict = "Break-even"
        verdict_color = "yellow"
    else:
        verdict = "Underperformer"
        verdict_color = "red"

    return {
        "spend_total": round(spend_total, 2),
        "spend_per_day": round(spend_per_day, 2),
        "days": days,
        "orders": orders,
        "revenue": round(revenue, 2),
        "cogs_total": round(cogs_total, 2),
        "net_profit": round(net_profit, 2),
        "cpa": round(cpa, 2),
        "roas": round(roas, 2),
        "roi": round(roi, 2),
        "profit_margin_pct": round(profit_margin_pct, 2),
        "break_even_roas": round(break_even_roas, 2),
        "margin_pct": round(margin * 100, 2),
        "verdict": verdict,
        "verdict_color": verdict_color,
        "cost_price": cost_price,
        "selling_price": selling_price
    }


@router.post("/metrics")
async def analyze_metrics(
    spend_total: float = Form(...),
    days: int = Form(...),
    orders: int = Form(...),
    cost_price: float = Form(...),
    selling_price: float = Form(...),
    creative: Optional[UploadFile] = File(None)
):
    """Business Metrics endpoint with optional creative analysis."""
    if orders <= 0:
        raise HTTPException(status_code=400, detail="Orders must be greater than 0.")
    if spend_total <= 0:
        raise HTTPException(status_code=400, detail="Spend must be greater than 0.")
    if selling_price <= cost_price:
        raise HTTPException(status_code=400, detail="Selling price must be greater than cost price.")

    metrics = calculate_metrics(spend_total, orders, cost_price, selling_price, days)

    ai_analysis = None
    creative_analyzed = False

    if creative and creative.filename:
        try:
            file_bytes = await creative.read()
            content_type = creative.content_type or "image/jpeg"

            processed_bytes = process_uploaded_file(file_bytes, content_type)
            if processed_bytes:
                image_b64 = encode_image_to_base64(processed_bytes)
                ai_analysis = await analyze_creative_performance(image_b64, metrics)
                creative_analyzed = True
        except Exception as e:
            print(f"Creative processing error: {e}")

    if not creative_analyzed:
        ai_analysis = await analyze_text_only_performance(metrics)

    return JSONResponse({
        "metrics": metrics,
        "ai_analysis": ai_analysis,
        "creative_analyzed": creative_analyzed,
        "status": "success"
    })
