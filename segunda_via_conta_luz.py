from pprint import pp

from playwright.async_api import async_playwright
from requests import post, get

import asyncio


async def playwright_access():
    async with async_playwright() as p:
        url = 'https://servicos.energisa.com.br/login'
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        print(await page.title())
        await page.get_by_role("textbox").fill('20443596859')
        await page.pause()
        await browser.close()


def baixar_pdf():
    cookies = {
    '_gid': 'GA1.3.961648134.1725013507',
    '_fbp': 'fb.2.1725013507716.977698556218039783',
    '_clck': '1oev70y%7C2%7Cfor%7C0%7C1703',
    'bm_sz': '374FCF844B44153C5FDBF9C64A9C71DA~YAAQCvYpF5DLvZqRAQAA2pp4pBg8UkacgG9DoVdVAW3i6MjTuXHMaBEvOZ89ICZ8IP5/LE8rXHLD8gJ1zq7iFkm59Z0dqh3eO+TB68B4Jdi/9Wgb7kEGuIul5+ChfskEfhvw8nVBCrye7VW3Idp3iR3cXB8mKWFa3sVn9b9syZyikPyjXcbGUw9+Xtc09yV8TBppNIMXaXrU3PUm0BBvEsIzEQ3Ef1CiwN6seft+3xaKn4bOYYqMqYTf6tnVZ283/RJEf548cbseZQx7QVr70CdtjSJf8gxbQ7jwg5JBoaWHCUaGGPB1T+R7ZzCPVPwrrOBDi43euiEnCI6/r3Ay7d8gUVm/DFWcF9ctmKt6GUtEI2b4ZkHLSlNJO++geXpAk0M+apkDrdxEbRiM/UccH2KI3k+6AGP3a4UrM+Hpkd+69edifGCcrwNJFx3wwhvIiTx1YP7RBEDAmx4q/3xvyX+9i9myEmmFMnOvVk7HJLyD~4600372~3686705',
    'bm_mi': '9A079EBBC8D32AE0B1E32067A5DF7FD2~YAAQDthJF5exe5GRAQAAMax5pBjTyHgJLFJ9ahNpcDROVDYVaZgNWiotmW671+VCZ5P0U3VabFLagHs+OXByStwZcOiJocPR1jCa1LG/uTChqcnsh+zOurmPzdRxLOw9fpU9d96Vqat+XQDJEZunpx1Eh4lGHvVvxMW1IHxzTeUd8l8scNoFx/iPlVERukawOPHzhj9+uggbvbFHQ1zponzC4DEKTr2NkCgM8vM7kUeaKsyx4wa+bgwRB/Qt+54/a/BFY5rPjViLCbn+bxtklRPqHxWmBLU1B/xrPWiVDczdGa/eDwOf7lN4jAaWv/lk~1',
    '_ga_JT7VJSPDK5': 'GS1.3.1725041316.2.1.1725041316.60.0.0',
    '_ga_X3RN62760T': 'GS1.3.1725041316.2.0.1725041316.60.0.0',
    'ak_bmsc': 'FB58C58B690945E2CCE6A19EE7B966E4~000000000000000000000000000000~YAAQDthJF0mze5GRAQAAbbJ5pBiCYG1qkPAIyWq1OSORBi9ae8fkS3oUW7H/Gh5blz6RWD+o40+afQrqSVuzOnXAvGePlrOW8lIizwIYa3YrJm9reuRMMM3zozyKQeU3wR1/nrYDjQNm36JKMiqqgHBQu9hno6Dylw9uWa387p0PfsXdAIbmrIqMMtkHc1YyPtR7t887iSTheDjDxPZhm/rO7WG5AwzeUUzECEDiB6E2CzDf8W/1JdjtpHRwsaxMBIhqDwKkQwuwb8nv9fQj3XK44kod4TA3ngOIGBvgFNMoB0j+24kr0nqD1LIBcsFAlPnFi1nka9Vw8+4xhFEwIlUIbPXZqC/ON3mmf7dbT7BHl0S4N6Q6C7CEq0NGgWLf4H7+RyDfCxYmy0BtnoTkaxFQ6motPKn8j4oLqixZzZJOCJDovSwT9KkQeB0kDEbrNUmyUXks1RYBxNw6q/qnm46W1CJnYDY4SNhq5cBcX1xFaLOGqLym848bLbIi9yem+bGfn+O545YKXA==',
    'CodEmpresa': '9',
    'MeuLocal': 'MeuEstadoExtenso=SÃ£o Paulo&MinhaCidade=PRESIDENTE PRUDENTE&MinhaCidadeID=1&MeuEstadoSigla=SP&MeuCodEmpresa=9',
    'AccessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IiE9IWVuYyE9IUwwNHI3NUtsVkVUcEYwNkNFSDRhS1E9PSIsInBhc3N3b3JkIjoiIT0hZW5jIT0hTDA0cjc1S2xWRVRwRjA2Q0VINGFLUT09IiwiY2hhdmVEZVNlZ3VyYW5jYSI6IiE9IWVuYyE9ISs1T3JJMXEvcm9TYjFjNktIdlBqcEE9PSIsImF1dGhTdGF0ZSI6IiE9IWVuYyE9IWpnMHhramk5R3hUMHdiU2puS3NoMVE9PSIsIm5hbWUiOiIhPSFlbmMhPSErNU9ySTFxL3JvU2IxYzZLSHZQanBBPT0iLCJzb2NpYWwiOiIhPSFlbmMhPSErNU9ySTFxL3JvU2IxYzZLSHZQanBBPT0iLCJjb21wQ29kZSI6IiE9IWVuYyE9ISs1T3JJMXEvcm9TYjFjNktIdlBqcEE9PSIsImlkZW50aXR5dHlwZSI6InVzZXIiLCJhdXRob3JpemVkQ0RDTGlzdCI6IiE9IWVuYyE9ISs1T3JJMXEvcm9TYjFjNktIdlBqcEE9PSIsInNlc3Npb25JZCI6IiE9IWVuYyE9IXZyS2NRcjlqdGFzaTY3LzdsWGQrZFAvZ1Zha09KOUhPak1hMU50Uml1S2M9IiwibmJmIjoxNzI1MDQxMzU0LCJleHAiOjE3MjUwNDI1NTQsImlhdCI6MTcyNTA0MTM1NCwiaXNzIjoiZW5lcmdpc2EiLCJhdWQiOiJlbmVyZ2lzYSJ9.AfLfPBSZMp0C-gPLRDlPFunFOnqYZabpox8KFKDLtIc',
    'primeiroAcesso': '1',
    'OptanonAlertBoxClosed': '2024-08-30T18:09:10.421Z',
    'OptanonConsent': 'isIABGlobal=false&datestamp=Fri+Aug+30+2024+15%3A09%3A10+GMT-0300+(Hora+padr%C3%A3o+de+Bras%C3%ADlia)&version=202210.1.0&hosts=&consentId=d5293a4e-3e60-46e5-a38b-174096702764&interactionCount=1&landingPath=NotLandingPage&groups=C0002%3A1%2CC0001%3A1%2CC0003%3A1',
    'LF3fHRAjveUqny8PdrxipHkZPYh69DqgJ8tkoB6p': 'Fe26.2*2*01327103ebe5881deac4d49050ef66e403318bd2da4afdf54f783cd3dacd308c*vrOhtJgumf8lLXop83ICfQ*BijHQVlvfa-dxc9XUCzZ0CZzsvmrvC7runqgo2uMqlqorvU6HgKrOu3bX40XGt8ZJBrGVbvlHG4MGGf5otQ3IkD7iycyxfSV1m33EAUtn3sDaloQwtiFBn3hDtZ5txD2PzqbJ9Bl9NDhqOeYpt1pE7Gsm-nCr2ZiLGQ7kCssMu4*1726337585145*9775bef166576bf96a120969a2578af83d8f1be357a18b400b5b82d502b60b29*wz0ZHgfvZwQLh6yvZOlxkcDbV-qgyjfYAXUivHZ4hKE',
    '_ga_WMNSR52TVF': 'GS1.1.1725041246.4.1.1725041740.0.0.0',
    '_ga': 'GA1.1.451642.1725013507',
    'bm_sv': '1D8D54CC59D7A77C277272F27AFE8D90~YAAQDthJF6B8fZGRAQAAeyyApBj+3ZX3RIg240JpWKdBltoxMa1ggrpnomuQo+QXwM1YcTPqtwrYRffIWXoeGsiQQYvL9yn/qCOWlrijbCQWDyd9IMVvrwcsIjUPoMkGuGOg9TQMWEGtyl8pU/DYI4mJqqISg7HIj35p64lcvvxxpet9Sz+jO/KlU6g+UR44f5ZtAXMYFWCIsULzJ+REz04DWP726gZjCdOprMJz0X879u3FtoOyKOdr+BGTmgAPdsFjGqzM~1',
    '_clsk': '1tlveof%7C1725041741726%7C11%7C1%7Cz.clarity.ms%2Fcollect',
    '_abck': '2D47FEF8F94F4ECA6AC46EEBC1277DE6~0~YAAQDthJF+GMfZGRAQAA4HOApAz7/+pp2+ZLSkvjUwywTg48ojFBO5RobdXacZte/UICa14QfV0xW6vK7+6jduxjF3qDwmeDicBLDo3NRc8g9so2352PtSBeGulryl3cND9FCh4eEPzo0Cmb2u6QimDedadQZ0OMCYaZi30hrQV3X/8OK3w6WLbyQZMYSJc8Q3DW8VSnJkvtC6f2ySkd/OdP8qko0RA/omWxpLkIF7bdaOB/B17Z34MpqX6/OfQM577g0Duf5AAi69p4WaC3sRAVocguuGGva4F82+urjB35cy4fjz2VZ1PFF546kTaBO8eLT1VR0en7F3yKeY/AyauoIKeHJ0+nhXDOL8yS3TygPIBLPqUtA7siS3Zu2dDo5gsffczDuzNsueYjlnheNFX/2UwgEQfaOu49lJW6MX71lWdj+srFkZ/IBy89/gymrcdCuRdQTSWs8D60gyFgzXeGK+uyZRAmNZMklptRVcY=~-1~-1~-1',
    '_dd_s': 'rum=0&expire=1725042751159',
}

    headers = {
    'accept': 'application/pdf',
    'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    # 'cookie': '_gid=GA1.3.961648134.1725013507; _fbp=fb.2.1725013507716.977698556218039783; _clck=1oev70y%7C2%7Cfor%7C0%7C1703; bm_sz=374FCF844B44153C5FDBF9C64A9C71DA~YAAQCvYpF5DLvZqRAQAA2pp4pBg8UkacgG9DoVdVAW3i6MjTuXHMaBEvOZ89ICZ8IP5/LE8rXHLD8gJ1zq7iFkm59Z0dqh3eO+TB68B4Jdi/9Wgb7kEGuIul5+ChfskEfhvw8nVBCrye7VW3Idp3iR3cXB8mKWFa3sVn9b9syZyikPyjXcbGUw9+Xtc09yV8TBppNIMXaXrU3PUm0BBvEsIzEQ3Ef1CiwN6seft+3xaKn4bOYYqMqYTf6tnVZ283/RJEf548cbseZQx7QVr70CdtjSJf8gxbQ7jwg5JBoaWHCUaGGPB1T+R7ZzCPVPwrrOBDi43euiEnCI6/r3Ay7d8gUVm/DFWcF9ctmKt6GUtEI2b4ZkHLSlNJO++geXpAk0M+apkDrdxEbRiM/UccH2KI3k+6AGP3a4UrM+Hpkd+69edifGCcrwNJFx3wwhvIiTx1YP7RBEDAmx4q/3xvyX+9i9myEmmFMnOvVk7HJLyD~4600372~3686705; bm_mi=9A079EBBC8D32AE0B1E32067A5DF7FD2~YAAQDthJF5exe5GRAQAAMax5pBjTyHgJLFJ9ahNpcDROVDYVaZgNWiotmW671+VCZ5P0U3VabFLagHs+OXByStwZcOiJocPR1jCa1LG/uTChqcnsh+zOurmPzdRxLOw9fpU9d96Vqat+XQDJEZunpx1Eh4lGHvVvxMW1IHxzTeUd8l8scNoFx/iPlVERukawOPHzhj9+uggbvbFHQ1zponzC4DEKTr2NkCgM8vM7kUeaKsyx4wa+bgwRB/Qt+54/a/BFY5rPjViLCbn+bxtklRPqHxWmBLU1B/xrPWiVDczdGa/eDwOf7lN4jAaWv/lk~1; _ga_JT7VJSPDK5=GS1.3.1725041316.2.1.1725041316.60.0.0; _ga_X3RN62760T=GS1.3.1725041316.2.0.1725041316.60.0.0; ak_bmsc=FB58C58B690945E2CCE6A19EE7B966E4~000000000000000000000000000000~YAAQDthJF0mze5GRAQAAbbJ5pBiCYG1qkPAIyWq1OSORBi9ae8fkS3oUW7H/Gh5blz6RWD+o40+afQrqSVuzOnXAvGePlrOW8lIizwIYa3YrJm9reuRMMM3zozyKQeU3wR1/nrYDjQNm36JKMiqqgHBQu9hno6Dylw9uWa387p0PfsXdAIbmrIqMMtkHc1YyPtR7t887iSTheDjDxPZhm/rO7WG5AwzeUUzECEDiB6E2CzDf8W/1JdjtpHRwsaxMBIhqDwKkQwuwb8nv9fQj3XK44kod4TA3ngOIGBvgFNMoB0j+24kr0nqD1LIBcsFAlPnFi1nka9Vw8+4xhFEwIlUIbPXZqC/ON3mmf7dbT7BHl0S4N6Q6C7CEq0NGgWLf4H7+RyDfCxYmy0BtnoTkaxFQ6motPKn8j4oLqixZzZJOCJDovSwT9KkQeB0kDEbrNUmyUXks1RYBxNw6q/qnm46W1CJnYDY4SNhq5cBcX1xFaLOGqLym848bLbIi9yem+bGfn+O545YKXA==; CodEmpresa=9; MeuLocal=MeuEstadoExtenso=SÃ£o Paulo&MinhaCidade=PRESIDENTE PRUDENTE&MinhaCidadeID=1&MeuEstadoSigla=SP&MeuCodEmpresa=9; AccessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IiE9IWVuYyE9IUwwNHI3NUtsVkVUcEYwNkNFSDRhS1E9PSIsInBhc3N3b3JkIjoiIT0hZW5jIT0hTDA0cjc1S2xWRVRwRjA2Q0VINGFLUT09IiwiY2hhdmVEZVNlZ3VyYW5jYSI6IiE9IWVuYyE9ISs1T3JJMXEvcm9TYjFjNktIdlBqcEE9PSIsImF1dGhTdGF0ZSI6IiE9IWVuYyE9IWpnMHhramk5R3hUMHdiU2puS3NoMVE9PSIsIm5hbWUiOiIhPSFlbmMhPSErNU9ySTFxL3JvU2IxYzZLSHZQanBBPT0iLCJzb2NpYWwiOiIhPSFlbmMhPSErNU9ySTFxL3JvU2IxYzZLSHZQanBBPT0iLCJjb21wQ29kZSI6IiE9IWVuYyE9ISs1T3JJMXEvcm9TYjFjNktIdlBqcEE9PSIsImlkZW50aXR5dHlwZSI6InVzZXIiLCJhdXRob3JpemVkQ0RDTGlzdCI6IiE9IWVuYyE9ISs1T3JJMXEvcm9TYjFjNktIdlBqcEE9PSIsInNlc3Npb25JZCI6IiE9IWVuYyE9IXZyS2NRcjlqdGFzaTY3LzdsWGQrZFAvZ1Zha09KOUhPak1hMU50Uml1S2M9IiwibmJmIjoxNzI1MDQxMzU0LCJleHAiOjE3MjUwNDI1NTQsImlhdCI6MTcyNTA0MTM1NCwiaXNzIjoiZW5lcmdpc2EiLCJhdWQiOiJlbmVyZ2lzYSJ9.AfLfPBSZMp0C-gPLRDlPFunFOnqYZabpox8KFKDLtIc; primeiroAcesso=1; OptanonAlertBoxClosed=2024-08-30T18:09:10.421Z; OptanonConsent=isIABGlobal=false&datestamp=Fri+Aug+30+2024+15%3A09%3A10+GMT-0300+(Hora+padr%C3%A3o+de+Bras%C3%ADlia)&version=202210.1.0&hosts=&consentId=d5293a4e-3e60-46e5-a38b-174096702764&interactionCount=1&landingPath=NotLandingPage&groups=C0002%3A1%2CC0001%3A1%2CC0003%3A1; LF3fHRAjveUqny8PdrxipHkZPYh69DqgJ8tkoB6p=Fe26.2*2*01327103ebe5881deac4d49050ef66e403318bd2da4afdf54f783cd3dacd308c*vrOhtJgumf8lLXop83ICfQ*BijHQVlvfa-dxc9XUCzZ0CZzsvmrvC7runqgo2uMqlqorvU6HgKrOu3bX40XGt8ZJBrGVbvlHG4MGGf5otQ3IkD7iycyxfSV1m33EAUtn3sDaloQwtiFBn3hDtZ5txD2PzqbJ9Bl9NDhqOeYpt1pE7Gsm-nCr2ZiLGQ7kCssMu4*1726337585145*9775bef166576bf96a120969a2578af83d8f1be357a18b400b5b82d502b60b29*wz0ZHgfvZwQLh6yvZOlxkcDbV-qgyjfYAXUivHZ4hKE; _ga_WMNSR52TVF=GS1.1.1725041246.4.1.1725041740.0.0.0; _ga=GA1.1.451642.1725013507; bm_sv=1D8D54CC59D7A77C277272F27AFE8D90~YAAQDthJF6B8fZGRAQAAeyyApBj+3ZX3RIg240JpWKdBltoxMa1ggrpnomuQo+QXwM1YcTPqtwrYRffIWXoeGsiQQYvL9yn/qCOWlrijbCQWDyd9IMVvrwcsIjUPoMkGuGOg9TQMWEGtyl8pU/DYI4mJqqISg7HIj35p64lcvvxxpet9Sz+jO/KlU6g+UR44f5ZtAXMYFWCIsULzJ+REz04DWP726gZjCdOprMJz0X879u3FtoOyKOdr+BGTmgAPdsFjGqzM~1; _clsk=1tlveof%7C1725041741726%7C11%7C1%7Cz.clarity.ms%2Fcollect; _abck=2D47FEF8F94F4ECA6AC46EEBC1277DE6~0~YAAQDthJF+GMfZGRAQAA4HOApAz7/+pp2+ZLSkvjUwywTg48ojFBO5RobdXacZte/UICa14QfV0xW6vK7+6jduxjF3qDwmeDicBLDo3NRc8g9so2352PtSBeGulryl3cND9FCh4eEPzo0Cmb2u6QimDedadQZ0OMCYaZi30hrQV3X/8OK3w6WLbyQZMYSJc8Q3DW8VSnJkvtC6f2ySkd/OdP8qko0RA/omWxpLkIF7bdaOB/B17Z34MpqX6/OfQM577g0Duf5AAi69p4WaC3sRAVocguuGGva4F82+urjB35cy4fjz2VZ1PFF546kTaBO8eLT1VR0en7F3yKeY/AyauoIKeHJ0+nhXDOL8yS3TygPIBLPqUtA7siS3Zu2dDo5gsffczDuzNsueYjlnheNFX/2UwgEQfaOu49lJW6MX71lWdj+srFkZ/IBy89/gymrcdCuRdQTSWs8D60gyFgzXeGK+uyZRAmNZMklptRVcY=~-1~-1~-1; _dd_s=rum=0&expire=1725042751159',
    'ispublic': '0',
    'origin': 'https://servicos.energisa.com.br',
    'priority': 'u=1, i',
    'referer': 'https://servicos.energisa.com.br/faturas/59124378',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

    json_data = {
    'codigoEmpresaWeb': 9,
    'cdc': 4554733,
    'digitoVerificadorCdc': 0,
    'ano': 2024,
    'mes': 7,
    'cdcRed': None,
    'fatura': 59124378,
    'ate': 'eyJhbGciOiJBMjU2S1ciLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwidHlwIjoiSldUIiwiY3R5IjoiSldUIn0.3qR9fUmcCFu0ZbqYtwnCQukky9GdpuYCg2sHUZpzYlfKmAGQXaB6FrE_MOTjp9QpLhRY6q8YkD5Af-hBVH7eNG2Bg-RRR26i.1V7u63hjNNRunRC7I8Z4Ig.e-KcRUmDqq3bPlYcXNTvtSSN1LlBHqVYOpVRu7mcssgnnPz14Pq3AvZSJ0KmqCk9TdQzzXBpCFzLMBVSjBCiw5RKswJrI6OY5-XHMfHuRL7tk3JNZ0iHQBXGwSDeQ-37-PxZzXTZrYnercIgY3m2tlFsRCKyBCPySk0C_yB7AKz_dK5rFoRyCIsk_caAQ-33Si0j9Tgi0xXypv0annUc1WmwsepoCTz899j0yPh7xePH9HhmSyYj6KI8sGfyw9h9mIz6MOY8Nr5kdjFkxxo-zNscgsFG3bTONLcjFTkAQd6bqWqa5mHleS0aYWD5VdVv6bWA6jtnZiGWMQwztj07sRJjfQA_CigC5VKA0GiM54UKRkfWK7tYEE2VR1Qvhk_hAruEu2Udn5h8kPWVKYsoATiSC1JB4Ro1YwivYOir1iuxhyjfi9scKO8pvkK3b_K0VwnDHYyFZJtWaVN1Y3G18usYdHkf7GDceNhqWsLXx-L3elYADYFgiplYt3bPj2qWctUHcu2LkjReKC1t6dnZI8Qla7nFng73ixkc1iYEAY3-QXNOxd07jN0BGxkkXhd0h_oppQBqm2aiIx40mxdgUzci_IIn9L5XZUx3eSKIA2PvNgHVDGEG-6NcsRFrkVJwyl7WOJuH9RfXPeSFH2PBconQJ80mVPd3Xy9up7MYPmeGSaIlPrewI3Ki3TngCUvYwpw0hGWDcnXRvnB869Pj4A0CxACBCsW1LGydqOyfFwuWY3D1VHDCIGfL1JeRsVyYlNDp10_bvOmKjna8jUDem0LqLeBfuSQdK18oIAxVrZ698PAu1BlO4w-wag_DlVJW6blveIIALW0VZ24HXfHm-nPAHRFOvZ6ept0lJk9zCtYLqy617IITq0jfbid7VQNMHNtvV_MV3qURg-emQQjpVPYIIk2wNN5zWtubJa4vtwVYmeSG_KGXh07iMtL293ePGjffDJNPndjwdV3xJi_bV6Qop1q50QRPZAszPo2mMSepf6uNShIgpOacYHY029bl.xKOqKX-MIvvhYBPpPUWl1ZGbgKyegbXd8uNDl3SOucE',
    'udk': 'EwBgLGDMCsCcBsAOOQ',
    'utk': 'eyJhbGciOiJBMjU2S1ciLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwidHlwIjoiSldUIiwiY3R5IjoiSldUIn0.p9kf9GntNN7GEwBGlbZ4FnU1vSZuhvJKvQRHPpTEMSLK7cCHy-rUEkLXMAWLNyw_1-4rIThTcMltbSsOzn1JSwHuDIcCwc9l.jWWGEiusICPUy_B9VjpW1w.B3Wz444mQOkupgbNq5lQsusbJkwyuuQnTGFmPMZK2cpZo0Z03SREjKTI2oDfrbSX9jZyJd5Z-hiAdsVfogspbZNIs0wprTfEIisk1rjEaldTvlBCkAG2NHCNoa-xn2YDjAgN87-R595TzTgPp0B3GlhvbHOTuSXKf6HvclSfxKBu27VwANpUxmSOOP-8UZXFem2vqP9PAFbMdC4zOkUXkNKaCPo8nptsylG30snq2PpndVN7mh7_zhHl76zXoIU_kq29Qpnpqd8oUbJI8UQg0BwJ69ery4Z7Ad9Tilos3xIM98kwN38eagNpzv054JSgUbktd_ASfM0pJ6Jb5OvZ-fQYYIUisk5pDt7l4-60GBNtPAttUFfOqSdLKdQxwv0kwxVUG7F5sVxHS4JmHWDNgDOwurL7KaSziF4bdxi--mFlxGsGLFKNgjG-3w0WoM1QNfSLwYDnGaShwYsKMjr30UL5eQbqgWT9vUFR1cPZU0wOEznFC0-2AkwiKSGA33ZFDmdQST7wnSxM2CEDrJL8vK-6RhwAitlBgE3ohw7h_UfKAnyL10wXHTQ3o11xRdShSZf73b9kqRl_W0Na8cJBgj-gEoDfJ3ffUAf0keF2EW5iC0ogeRzJJED2yPEy-tjhBeoA0kmIsafcy7nGN0OZNlVALooaKrnz2C6ZP08VvgoxK7hKXR77xZsBX5ZRrpjL77k0SHx_9jNli4fvVkQOjtJv44TqoyKc4iOg2DZQDFbxbrrfjPcN5vi0bhc4zKXYM6JFr6s-3NU_8dADCMpzXa253Q60oEpu1_R3k6jhsX3ELVDaVmhQtBzoSSIK2scZIZ8Jd5bqmmHirha1cUGleLXje5cB3WfcDKZkSybUwEvsuQaFa2vTbbCxJasA3ut1oO1HvyL0lYkLCqXWOKeq7rD2gahBVgpi0MswaMVWFjj-989FfO6HblW5H5XUsWYxDFz_3bq4VE3mdJnqsereHXT2BVxL4HQObTEh8i2TcqIf7tQm_fx89z2as3ydYb94vTVRys0b07eZjhADr5DI4-B-lSa20xkF1XQpQ-kpgOiXJZcaHei1gyAxpnIi3giBOPLkWeN9tQBQqGUGtbniPuGUM6gXTWXgcXMaABniNChn5AixTbFOM7WvujlHXAz13pL2OXQDP5nZ_U5Nma6T6VcsLEdewseXXoDjl103sTJfRtqp_jUTT70ZVPPs7_FxazHBXfe5qLEUuvzrAriAOw.Y08J39rE8jiku9W3un192CS6OrK5RnAepqgV4JMhm2U',
    'refreshToken': '04ab39088400d4650633b1fee7be155395e4a46508f6cb0dd43b808acdd6121978de7241116566b04bfa62a621fe9c1d1eb723409de670b75a4369dac1b750ea',
    'retk': '',
    }
    
    response = post(
        'https://servicos.energisa.com.br/api/clientes/SegundaVia/Download',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    # filename = 'conta_de_luz_082024.pdf'
    # with open(filename, 'wb') as f:
    #     f.write(response.content)
    print(response.status_code)


if __name__ == '__main__':
    asyncio.run(playwright_access())
    # baixar_pdf()
