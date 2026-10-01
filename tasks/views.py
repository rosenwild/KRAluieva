from django.shortcuts import render
from django.http import JsonResponse
from .data_loader import load_dataset


def index(request):
    return render(request, "tasks/index.html")


def get_plot_data(request):
    df = load_dataset()

    threshold = float(request.GET.get("threshold", 0.5))
    vm_filter = request.GET.get("vm_id", "all")

    if vm_filter != "all":
        df = df[df["vm_id"] == vm_filter]

    filtered_df = df[df["isolation_score"] <= threshold]

    records = df.copy()
    records["timestamp"] = records["timestamp"].dt.strftime("%Y-%m-%d %H:%M")

    return JsonResponse(
        {
            "records": records.to_dict(orient="records"),
            "threshold": threshold,
            "filtered_count": int(len(filtered_df)),
            "total_count": int(len(df)),
            "threats": filtered_df["vm_id"].unique().tolist(),
        }
    )
