"""Simpl Ops public dashboard mockup.

Run with:
    streamlit run examples/dashboard_mockup.py

This file uses fake sample data and safe demo logic only. It is not the
production Simpl Ops dashboard.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st

from signal_engine_demo import OperationalSnapshot, evaluate_snapshot

DATA_PATH = Path(__file__).parent / "data" / "no_pii_operational_sample.csv"


@st.cache_data
def load_data() -> pd.DataFrame:
    """Load fake demo data from the local repository."""

    return pd.read_csv(DATA_PATH)


st.set_page_config(page_title="Simpl Ops Portfolio Demo", layout="wide")

st.title("Simpl Ops — Portfolio Dashboard Mockup")
st.caption(
    "Public-safe replica using fake data and generic demo logic. Production code, "
    "private scoring, integrations, customer records, and advisory logic are not included."
)

source = load_data()
client_ids = source["client_id"].tolist()
selected_client = st.selectbox("Choose a fake demo client", client_ids)
row = source[source["client_id"] == selected_client].iloc[0]

snapshot = OperationalSnapshot(
    client_id=row["client_id"],
    business_type=row["business_type"],
    leads=int(row["leads"]),
    bookings=int(row["bookings"]),
    available_slots=int(row["available_slots"]),
    completed_jobs=int(row["completed_jobs"]),
    follow_up_tasks=int(row["follow_up_tasks"]),
    avg_response_hours=float(row["avg_response_hours"]),
)

signals = evaluate_snapshot(snapshot)

st.subheader("Fake Operating Snapshot")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Leads", snapshot.leads)
col2.metric("Bookings", snapshot.bookings)
col3.metric("Available Slots", snapshot.available_slots)
col4.metric("Completed Jobs", snapshot.completed_jobs)
col5.metric("Follow-Ups", snapshot.follow_up_tasks)

st.subheader("Public Demo Signal Summary")
for signal in signals:
    with st.container(border=True):
        st.write(f"**{signal.signal_name}**")
        st.write(f"Status: `{signal.status}` | Value: `{signal.value}`")
        st.info(signal.summary)

st.subheader("Owner-Facing Next Action Placeholder")
st.write(
    "In the private product, this area translates operational signals into prioritized "
    "owner guidance. This public portfolio demo uses generic placeholder language only."
)

st.subheader("Security Boundary")
st.write(
    "This demo intentionally excludes production integrations, live data sources, "
    "private scoring, customer records, access-control details, and proprietary advisory logic."
)
