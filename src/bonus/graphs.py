import matplotlib.pyplot as graph
import logging
from pathlib import Path

PLOTS_ROOT = Path(__file__).resolve().parents[2] / "plots"

def show_data_distribution(km: list[int], price: list[int]) -> None:
    graph.figure()
    graph.figure()
    graph.style.use('default')

    graph.plot(km,price, 'bo')
    graph.xlabel("Km")
    graph.ylabel("Price")
    graph.title("Data Distribution")
    #graph.show()
    save_graph("data_distribution.png")
    graph.close()


def show_data_line(km: list[int], price: list[int], theta0, theta1) -> None:

    graph.style.use('default')
    graph.figure()

    graph.plot(km,price, 'bo')
    graph.axline((0,theta0), slope= theta1)
    graph.xlabel("Km")
    graph.ylabel("Price")
    graph.title("Line")
    #graph.show()
    save_graph("line.png")
    graph.close()

def show_cost(iterations: list[float], cost: list[float]) -> None:
    
    graph.style.use('default')
    graph.figure()

    graph.plot(iterations, cost)
    # make an other line with thetas
    graph.xlabel("Epoch")
    graph.ylabel("Cost")
    graph.yscale("log")
    graph.title("How well")
    save_graph("cost.png")
    graph.close()

def save_graph(filename: str, tight: bool = True) -> Path:
    out_dir = PLOTS_ROOT
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / filename
    if tight:
        graph.tight_layout()
    graph.savefig(out_path)
    logging.info(f"Saved plot to {out_path}")
    return out_path


"""
def save_graph(subdir: str, filename: str, tight: bool = True) -> Path:
    out_dir = PLOTS_ROOT / subdir
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / filename
    if tight:
        graph.tight_layout()
    graph.savefig(out_path)
    logging.info(f"Saved plot to {out_path}")
    return out_path
    """