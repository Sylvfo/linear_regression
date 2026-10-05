import matplotlib.pyplot as graph

def show_data_distribution(km: list[int], price: list[int]) -> None:

    graph.style.use('default')

    graph.plot(km,price, 'bo')
    graph.xlabel("Km")
    graph.ylabel("Price")
    graph.title("Data Distribution")
    graph.show()


def show_data_line(km: list[int], price: list[int], theta0, theta1) -> None:

    graph.style.use('default')

    graph.plot(km,price, 'bo')
    # make an other line with thetas
    graph.plot(theta0,theta1)
    graph.xlabel("Km")
    graph.ylabel("Price")
    graph.title("Line")
    graph.show()