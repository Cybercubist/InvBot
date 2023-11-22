import requests
from math import sqrt

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"

def finAPI(ticker):
    try:
        querystring = {"symbol":"AMRN","region":"US"}
        querystring["symbol"] = ticker

        headers = {
        'x-rapidapi-key': "YOUR_RAPID_API_KEY",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        stockdata = response.json()

        price = stockdata['price']
        regularMarketPrice = price['regularMarketPrice']
        currentPrice = regularMarketPrice['raw']
        marketCap = price['marketCap']
        currentMC = marketCap['raw']
        stockname = price['shortName']

        incomeQuarterly = stockdata['incomeStatementHistoryQuarterly']
        incomeQuarterly2 = incomeQuarterly['incomeStatementHistory']

        i = 0
        TTMRevenue = 0
        TTMIncome = 0
        TTMGross = 0
        TTMresearchDevelopment = 0
        while i < 4:
            incomeQuarterly3 = incomeQuarterly2[i]
            QRevenue = incomeQuarterly3['totalRevenue']
            QIncome = incomeQuarterly3['netIncome']
            QGross = incomeQuarterly3['grossProfit']
            QresearchDevelopment = incomeQuarterly3['researchDevelopment']
            TTMRevenue = TTMRevenue + QRevenue['raw']
            TTMIncome = TTMIncome + QIncome['raw']
            TTMGross = TTMGross + QGross['raw']
            try:
                TTMresearchDevelopment = TTMresearchDevelopment + QresearchDevelopment['raw']
            except Exception:
                TTMresearchDevelopment = 0
            i = i+1

        PtoE = currentMC/TTMIncome
        PtoS = currentMC/TTMRevenue

        GrossMargin = TTMGross/TTMRevenue*100

        incomedata = stockdata['incomeStatementHistory']
        incomedata2 = incomedata['incomeStatementHistory']
        incomedata3 = incomedata2[3]
        oldRevenue = incomedata3['totalRevenue']
        oldRevenueRaw = oldRevenue['raw']
        growthTempo = (TTMRevenue/oldRevenueRaw)
        growthTempo = (sqrt(sqrt(growthTempo))-1)*100

        analytics = ''

        oldGrossIncome = incomedata3['grossProfit']
        oldGrossIncomeRaw = oldGrossIncome['raw']
        oldGrossMargin = oldGrossIncomeRaw/oldRevenueRaw*100

        Qbalancedata = stockdata['balanceSheetHistoryQuarterly']
        Qbalancedata2 = Qbalancedata['balanceSheetStatements']
        Qbalancedata3 = Qbalancedata2[1]
        totalLiab = Qbalancedata3['totalLiab']
        totalLiabRaw = totalLiab['raw']
        totalEquity = Qbalancedata3['totalStockholderEquity']
        totalEquityRaw = totalEquity['raw']
        DtoE = totalLiabRaw/totalEquityRaw
 
        if PtoE > 0 and PtoE*PtoS < 50:
            analytics = analytics + "\n\U00002795 Low ratios!"
        if growthTempo > 30:
            analytics = analytics + "\n\U00002795 Very fast growing."
        if oldGrossMargin < GrossMargin:
            analytics = analytics + "\n\U00002795 Gross margin increases."
        if DtoE < 2 and DtoE > 0:
            analytics = analytics + "\n\U00002795 Moderate or low debt."

        if PtoE > 0 and PtoE*PtoS > 600:
            analytics = analytics + "\n\U00002757 Pricey by ratios!"
        if growthTempo < 0: 
            analytics = analytics + "\n\U00002757 Revenue decreases!"
        if oldGrossMargin > GrossMargin:
            analytics = analytics + "\n\U00002757 Gross margin decreases."
        if DtoE > 8 and DtoE > 0:
            analytics = analytics + "\n\U00002757 High debt."
        elif DtoE < 0:
            analytics = analytics + "\n\U00002757 Negative Debt-to-Equity!"

        currentMC = currentMC/1000000
        currentMC = round(currentMC, 0)
        TTMRevenue = TTMRevenue/1000000
        TTMIncome = TTMIncome/1000000
        TTMresearchDevelopment = TTMresearchDevelopment/1000000
        PtoE = round(PtoE)
        PtoS = round(PtoS,1)
        GrossMargin = round(GrossMargin, 1)
        growthTempo = round(growthTempo, 1)
        oldGrossMargin = round(GrossMargin, 1)


        Summary = ('\nAsset info ' + str(stockname) + ': \nAsset price, $:'+ str(currentPrice)
        + '\nMarket Cap, mln $: ' + str(currentMC) + '\nRevenue TTM, mln $: '
        + str(TTMRevenue) + '\nR&D TTM, mln $:'
        + str(TTMresearchDevelopment) + '\nNet income TTM, млн $: ' + str(TTMIncome)
        + '\nP/E=' + str(PtoE)+'\nP/S=' + str(PtoS) + '\nGross Income, %: ' + str(GrossMargin)
        + '\nRevenue growth rate, %: ' + str(growthTempo)) + '\n' + analytics

    except Exception:
        Summary = ("\nI don't know this asset! Please, try again...")
    
    return Summary

Ideas = ["<b>Investment idea №1: CareDx.</b>\n\n<b>Date:</b> 26.03.2023\n<b>Asset class:</b> US Stocks\n\nMany risky assets were squeezed last year. And because of the recent banking crisis they are still suffering now. But everything comes to an end and this situation shouldn't be an exception. At such chaotic market we still like risky assets, especially those one, which have fallen sharply recently. And #CDNA is one of them!"
         +"\n\nCareDx is a highly innovative healthcare company, that offers products and solutions for transplant patients. Genetic testing for post-transplant surveillance, AI-tools which calculates kidney rejection likelihood, cell therapy, telehealth monitoring solutions for pre- and post-transplant care. The company tries to be as innovative as possible."
         +"\n\nEven if it's operating income is below zero now, we believe that with current P/S = 1.5, strong cash positions and innovation kit, CareDx may be a solid investment at this point. You can also note here the fact, that company gross margin is good, and losses partly comes from high R&D spending.\n\n<i>Not an investment advice, all market losses is your own responsibility!</i>", 
         "<b>Investment idea №2: Compugen.</b>\n\n<b>Date:</b> 19.03.2023\n<b>Asset class:</b> US Stocks\n\nIn these unstable and gloomy conditions we still like risky assets. Yes, we shouldn't expect their coming back to 2020-2021 levels, at least not now. But they may be seriously underestimated at this point anyway."
         +"\n\nThis time we recommend you consider Compugen #CGEN again. The company has tiny market capitalization, which is even lower than it's cash&cash equivalents now. Also CGEN burns cash quite carefully, unlike many other companies of this type."
         +"\n\nIn Compugen we do like it's potential scalability, because the company uses some predictive computational  platform to find new antibodies. Also company's pipeline is pretty wide for it's MC and size. We can't guarantee your success, but at least you get decent chances here!\n\n<i>Not an investment advice, all market losses is your own responsibility!</i>",
         "<b>Investment idea №3: Pure Storage.</b>\n\n<b>Date:</b> 19.03.2023\n<b>Asset class:</b> US Stocks\n\nGrowth stocks weren't in favor lately, but there are still many opportunities. We believe you should consider techs of any size now, either you long-term investor or short-term speculative player."
         +"\n\nPure Storage #PSTG is one of our favorite picks in this sector. The company is balanced in many ways: not too big, not too small, not too value and not too cash-bleeding, both software and hardware. With P/S = 2.6 we believe PSTG should be pretty underestimated here."
         +"\n\nAlso we do like technology kit of Pure Storage and it's position in current trends. It offers flash array which can be crucial in AI, metaverse and cloud service development in future. If you need tech company with no weaknesses, it may be the case!\n\n<i>Not an investment advice, all market losses is your own responsibility!</i>",
         "<b>Investment idea №4: Trust Wallet Token.</b>\n\n<b>Date:</b> 19.03.2023\n<b>Asset class:</b> Crypto\n\nAfter last events in banking sector we know for sure: banks are not as safe as we could think. The task of saving your money nowadays may be tricky and one of ways is cryptocurrency. But to hold it on exchanges isn't a good idea and that's where cold wallets come!"
         +"\n\n#TWT is a token of very popular cold crypto wallet. On this wallet you can storage many different coins or add your own token. Trust Wallet may be the best of it's kind, especially when we talk about usability and coin assortment."
         +"\n\nWe don't know for sure, how the token itself will be used in future. But we believe the opportunity of integration of cold wallet and other crypto tools is pretty wide. If it's going to be better version of Metamask, upside may be impressive.\n\n<i>Not an investment advice, all market losses is your own responsibility!</i>",
         "<b>Investment idea №5: Nakamoto Games.</b>\n\n<b>Date:</b> 26.02.2023\n<b>Asset class:</b> Crypto\n\nWe all love crypto gems, because they can gift you fantastical x's. We believe that current market conditions are very good to make brave moves, so we try it."
         +"\n\nCasual games is a huge market and we see in Play-to-earn model good opportunities. The platform is going to develop mobile app soon and it may become a real gamechanger. Even if there is a risk of complete fail, our chances here should be still good.\n\n<i>Not an investment advice, all market losses is your own responsibility!</i>",
         "Top-5 investment ideas for <b>26.03.2023</b>:\n\n1. CareDx\n2. Compugen\n3. Pure Storage\n4. Trust Wallet Token\n5. Nakamoto Games\n\n<i>Not an investment advice, all market losses is your own responsibility!</i>"
        ]

Markets = ["<b>Market conditions 09.04.2023.</b>"
        +"\n\nThe start of April looks good. Even if NASDAQ didn't go higher last week, there was no significant correction. Conversely, on the weekly chart we see a considerable downside shade, which may tell us, that tech index is not going lower for now. So, our optimism about NASDAQ is still here and we prepare for even higher levels soon."
        +"\n\nOn the commodity side, we saw a good rebound of oil prices on news about OPEC cuts. However, after Monday jump oil prices didn't rush to go higher than Brent's 85$. Market conditions are still unclear: inflation is high and the banking crisis hasn't disappeared yet. "
        +"\n\nDJ Commodity is stagnating near the 1000 points level, but silver showed another good week and now is higher than 25$. Gold is strong too, staying beyond $2k."
        +"\n\nCryptocurrency was mixed last week. Ethereum +1%, Bitcoin -0.5%; altcoins didn't have any obvious direction. Overall, last few weeks were good for main coins and bad for the most altcoins. It looks like now everything here is close to it's fair price."
        +"\n\nNASDAQ last weeks growth was mainly due to blue chips strength. Though many risky assets are close to their historical lows or even still in 2 year downtrend. We see some opportunity here, that you can try to use."
        +"\n\nWe still believe in strong April. Since our oil&gas idea has already played out and small cap players fell behind of blue chips, we think, that now you should really consider tiny risky companies. Small biotechs look especially good, because stocks of this kind now on their historical lows and in full depression. So, focus here may be very profitable, try not to ignore it!"
        +"\n\n<i>Not an investment advice, all market losses is your own responsibility!</i>" 
          ]

Whatsnew = "<b>25.02.2023:</b> InvBot was born!\n<b>26.02.2023:</b> New 'Market conditions' feature!\n<b>02.04.2023:</b>New Market conditions note!\n\nBack to menu! -> /menu"