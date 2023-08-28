from app.src.use_cases import CreateStocksPlotUseCase

def main():
    plt = CreateStocksPlotUseCase()
    plt.create_stocks_plot()
    plt.calculate_stock_ema()


if __name__ == '__main__':
    main()
