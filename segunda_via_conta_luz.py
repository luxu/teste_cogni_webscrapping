from pprint import pp
from time import sleep

from playwright.async_api import async_playwright
from requests import post, get

import asyncio


async def playwright_access():
    async with async_playwright() as p:
        url = 'https://servicos.energisa.com.br/login'
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        await page.get_by_role("textbox").fill('')
        sleep(5)
        await page.get_by_role("button", name="ENTRAR").click()
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
    'primeiroAcesso': '1',
    'OptanonAlertBoxClosed': '2024-08-30T18:09:10.421Z',
    'OptanonConsent': 'isIABGlobal=false&datestamp=Fri+Aug+30+2024+15%3A09%3A10+GMT-0300+(Hora+padr%C3%A3o+de+Bras%C3%ADlia)&version=202210.1.0&hosts=&consentId=d5293a4e-3e60-46e5-a38b-174096702764&interactionCount=1&landingPath=NotLandingPage&groups=C0002%3A1%2CC0001%3A1%2CC0003%3A1',
    '_ga_WMNSR52TVF': 'GS1.1.1725043785.5.1.1725044819.0.0.0',
    '_ga': 'GA1.1.451642.1725013507',
    'LF3fHRAjveUqny8PdrxipHkZPYh69DqgJ8tkoB6p': 'Fe26.2*2*0efe8cd208edc2c8afb1b9015baabf23ecc5baca9f4c120bafe9c3cf012b666c*gwy7LsahA2l1f5msZfDAng*HN70IZN3nJvxLQc6kCtjklJEetP9nWz_P6H4uzZ1PP_RAoaqv8I9tlzxolTXCl3CwUempXxv_k7W-u6L88RToG7X9SGhFDuPgZF6dZGhVxufLOyu9xldYTaJKcvVNJEQv_iHVjI6H4y6FkPnaehErDevsxt6qw8LE9AM8mGJmpM*1726340976220*630e7bb96648e73c7cd0fc11d2db09af17413ece37ffccf9dd5c72ad972aa360*hvl7IYtvgccNzhq5sIAq_7-Bjt9igYNXiC3Dw0-sR0k',
    '_gat': '1',
    '_clsk': '1tlveof%7C1725045030149%7C33%7C1%7Cz.clarity.ms%2Fcollect',
    'bm_sv': '1D8D54CC59D7A77C277272F27AFE8D90~YAAQp8kQAvQCj5mRAQAAC1+ypBjm4BOxC+12BRgbE4FsCOoMZZUgKo5EMJUUMXsGZ8EvPv7B/5E5wXx61RJfgGEuNzxR3NFNTkunGW6vF/J1vJ+5NBe5F4TZYUxHgbvqzERO14c3fEclCfspJxqR9IRiEzV2l2z/UYGJ27VdeuigyS/bceSd0pWKPTIweorF41sQOh0EuYm9CQYmiB+8KvUp1AUMnnYtnqi+qhmIPuKJ3wnLkZdGO3hwCLq6vGmUU8QmxEyL~1',
    '_abck': '2D47FEF8F94F4ECA6AC46EEBC1277DE6~0~YAAQp8kQAiMUj5mRAQAAYOyypAybZ6U6BEXtva7PV1MTNDNCpAwjrKpLHNZcbVzSyHTaGDInvvF16Tptinxm4lDxO+MDtnsTdeb1loMRYcJCLx2+lJKWjtGnm83EpdIXzUZBF1m7Fc3xWf45njjst9QIXgv0F0ebe8WElMy37fGtDkGRvpLz+Jtv3LzAzVVjZSlWeyxYShMyzhHIwMii+7YazHxjuHCxeoICyth5PW9aR9XBexiVWCq+x6eHkVTRfKA0JnV3G5pjBsnah/uhNmns42lKeqAK0904aPc/6ERmi9D4/GadkU5cyYltYUlTw7P2uQkfKij862qGM1iFXusllMjoqdRC54mhG18abEKoSpQvLZavmcHX37ZfKsnJc6UhANDVntZiYBRfH7mJ2N+TW/1aNSnCXjsra8ELM6lxGIakN5/Mf/s6etBW4Ad4Q+3pizTCcbu7f52nIXUD6aHY/JK/ez1KjFGIaYfxfD4=~-1~-1~-1',
    '_dd_s': 'rum=0&expire=1725045976851',
    }

    headers = {
        'accept': 'application/pdf',
        'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': '_gid=GA1.3.961648134.1725013507; _fbp=fb.2.1725013507716.977698556218039783; _clck=1oev70y%7C2%7Cfor%7C0%7C1703; bm_sz=374FCF844B44153C5FDBF9C64A9C71DA~YAAQCvYpF5DLvZqRAQAA2pp4pBg8UkacgG9DoVdVAW3i6MjTuXHMaBEvOZ89ICZ8IP5/LE8rXHLD8gJ1zq7iFkm59Z0dqh3eO+TB68B4Jdi/9Wgb7kEGuIul5+ChfskEfhvw8nVBCrye7VW3Idp3iR3cXB8mKWFa3sVn9b9syZyikPyjXcbGUw9+Xtc09yV8TBppNIMXaXrU3PUm0BBvEsIzEQ3Ef1CiwN6seft+3xaKn4bOYYqMqYTf6tnVZ283/RJEf548cbseZQx7QVr70CdtjSJf8gxbQ7jwg5JBoaWHCUaGGPB1T+R7ZzCPVPwrrOBDi43euiEnCI6/r3Ay7d8gUVm/DFWcF9ctmKt6GUtEI2b4ZkHLSlNJO++geXpAk0M+apkDrdxEbRiM/UccH2KI3k+6AGP3a4UrM+Hpkd+69edifGCcrwNJFx3wwhvIiTx1YP7RBEDAmx4q/3xvyX+9i9myEmmFMnOvVk7HJLyD~4600372~3686705; bm_mi=9A079EBBC8D32AE0B1E32067A5DF7FD2~YAAQDthJF5exe5GRAQAAMax5pBjTyHgJLFJ9ahNpcDROVDYVaZgNWiotmW671+VCZ5P0U3VabFLagHs+OXByStwZcOiJocPR1jCa1LG/uTChqcnsh+zOurmPzdRxLOw9fpU9d96Vqat+XQDJEZunpx1Eh4lGHvVvxMW1IHxzTeUd8l8scNoFx/iPlVERukawOPHzhj9+uggbvbFHQ1zponzC4DEKTr2NkCgM8vM7kUeaKsyx4wa+bgwRB/Qt+54/a/BFY5rPjViLCbn+bxtklRPqHxWmBLU1B/xrPWiVDczdGa/eDwOf7lN4jAaWv/lk~1; _ga_JT7VJSPDK5=GS1.3.1725041316.2.1.1725041316.60.0.0; _ga_X3RN62760T=GS1.3.1725041316.2.0.1725041316.60.0.0; ak_bmsc=FB58C58B690945E2CCE6A19EE7B966E4~000000000000000000000000000000~YAAQDthJF0mze5GRAQAAbbJ5pBiCYG1qkPAIyWq1OSORBi9ae8fkS3oUW7H/Gh5blz6RWD+o40+afQrqSVuzOnXAvGePlrOW8lIizwIYa3YrJm9reuRMMM3zozyKQeU3wR1/nrYDjQNm36JKMiqqgHBQu9hno6Dylw9uWa387p0PfsXdAIbmrIqMMtkHc1YyPtR7t887iSTheDjDxPZhm/rO7WG5AwzeUUzECEDiB6E2CzDf8W/1JdjtpHRwsaxMBIhqDwKkQwuwb8nv9fQj3XK44kod4TA3ngOIGBvgFNMoB0j+24kr0nqD1LIBcsFAlPnFi1nka9Vw8+4xhFEwIlUIbPXZqC/ON3mmf7dbT7BHl0S4N6Q6C7CEq0NGgWLf4H7+RyDfCxYmy0BtnoTkaxFQ6motPKn8j4oLqixZzZJOCJDovSwT9KkQeB0kDEbrNUmyUXks1RYBxNw6q/qnm46W1CJnYDY4SNhq5cBcX1xFaLOGqLym848bLbIi9yem+bGfn+O545YKXA==; CodEmpresa=9; MeuLocal=MeuEstadoExtenso=SÃ£o Paulo&MinhaCidade=PRESIDENTE PRUDENTE&MinhaCidadeID=1&MeuEstadoSigla=SP&MeuCodEmpresa=9; primeiroAcesso=1; OptanonAlertBoxClosed=2024-08-30T18:09:10.421Z; OptanonConsent=isIABGlobal=false&datestamp=Fri+Aug+30+2024+15%3A09%3A10+GMT-0300+(Hora+padr%C3%A3o+de+Bras%C3%ADlia)&version=202210.1.0&hosts=&consentId=d5293a4e-3e60-46e5-a38b-174096702764&interactionCount=1&landingPath=NotLandingPage&groups=C0002%3A1%2CC0001%3A1%2CC0003%3A1; _ga_WMNSR52TVF=GS1.1.1725043785.5.1.1725044819.0.0.0; _ga=GA1.1.451642.1725013507; LF3fHRAjveUqny8PdrxipHkZPYh69DqgJ8tkoB6p=Fe26.2*2*0efe8cd208edc2c8afb1b9015baabf23ecc5baca9f4c120bafe9c3cf012b666c*gwy7LsahA2l1f5msZfDAng*HN70IZN3nJvxLQc6kCtjklJEetP9nWz_P6H4uzZ1PP_RAoaqv8I9tlzxolTXCl3CwUempXxv_k7W-u6L88RToG7X9SGhFDuPgZF6dZGhVxufLOyu9xldYTaJKcvVNJEQv_iHVjI6H4y6FkPnaehErDevsxt6qw8LE9AM8mGJmpM*1726340976220*630e7bb96648e73c7cd0fc11d2db09af17413ece37ffccf9dd5c72ad972aa360*hvl7IYtvgccNzhq5sIAq_7-Bjt9igYNXiC3Dw0-sR0k; _gat=1; _clsk=1tlveof%7C1725045030149%7C33%7C1%7Cz.clarity.ms%2Fcollect; bm_sv=1D8D54CC59D7A77C277272F27AFE8D90~YAAQp8kQAvQCj5mRAQAAC1+ypBjm4BOxC+12BRgbE4FsCOoMZZUgKo5EMJUUMXsGZ8EvPv7B/5E5wXx61RJfgGEuNzxR3NFNTkunGW6vF/J1vJ+5NBe5F4TZYUxHgbvqzERO14c3fEclCfspJxqR9IRiEzV2l2z/UYGJ27VdeuigyS/bceSd0pWKPTIweorF41sQOh0EuYm9CQYmiB+8KvUp1AUMnnYtnqi+qhmIPuKJ3wnLkZdGO3hwCLq6vGmUU8QmxEyL~1; _abck=2D47FEF8F94F4ECA6AC46EEBC1277DE6~0~YAAQp8kQAiMUj5mRAQAAYOyypAybZ6U6BEXtva7PV1MTNDNCpAwjrKpLHNZcbVzSyHTaGDInvvF16Tptinxm4lDxO+MDtnsTdeb1loMRYcJCLx2+lJKWjtGnm83EpdIXzUZBF1m7Fc3xWf45njjst9QIXgv0F0ebe8WElMy37fGtDkGRvpLz+Jtv3LzAzVVjZSlWeyxYShMyzhHIwMii+7YazHxjuHCxeoICyth5PW9aR9XBexiVWCq+x6eHkVTRfKA0JnV3G5pjBsnah/uhNmns42lKeqAK0904aPc/6ERmi9D4/GadkU5cyYltYUlTw7P2uQkfKij862qGM1iFXusllMjoqdRC54mhG18abEKoSpQvLZavmcHX37ZfKsnJc6UhANDVntZiYBRfH7mJ2N+TW/1aNSnCXjsra8ELM6lxGIakN5/Mf/s6etBW4Ad4Q+3pizTCcbu7f52nIXUD6aHY/JK/ez1KjFGIaYfxfD4=~-1~-1~-1; _dd_s=rum=0&expire=1725045976851',
        'ispublic': '0',
        'origin': 'https://servicos.energisa.com.br',
        'priority': 'u=1, i',
        'referer': 'https://servicos.energisa.com.br/faturas',
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
        'utk': 'eyJhbGciOiJBMjU2S1ciLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwidHlwIjoiSldUIiwiY3R5IjoiSldUIn0.v7DH3ySJfQsjbCPlCmJtpzelph0UGTQeGVxuA-c8OGfkdHF1VCB0VRibqnd7QzOwk1JPhPrcV-myJghQ-UCg6CAKuuaFSdh3.Y8s18RcEQBEab0L9i6SLOA.3pbtvZiCvdIX3i_UDLqu_7JssSKzvy8NF-SqsEYninQM1_gPDhX37-DsDPiJyV8_Idh2m9LM-v_sHuDvlgi33lNTjzj5xpFTlkitUo2DLsa_HicRAsX0TezUTf9128Bajv9-pWf0I8Y3Utld-ud6bKsmBX86R9-K2oJ1s0cIK4p84FMKXW8jS-pj4qbP1zOYvqrU42dWzkclzn7EKrl6vOZQ8tBygdeR5SpnFfoh6ELDBq6bXH2XZ2QYdhQ3W1-iQsSkjR_Vu_vySaUuxJeF6CXEsn6bA8zDNDoW1quswic0A7rfpurhHn9YhJrdyVb9GeNWZYkxPgXgl_rW1Tys6XyRsFM69ID45_JQzMutaJxCjfzUDqEd5ZKp18Snii8ZS7tkkNd3Me8xLv9LgPFPrP7I0gnHIzgVMjjY7Q9GuXiughCCrlncIdRlL2CwMxq6CDqU1LiqB57IAgKkWpcQzualyEiMhMJf0588lQQ2LKo5TnYjiFmaV_vESXHrVie5P1AZC4jJ-Fg6yVJs6LCptUNYIy3bq7n-i1_u4RSZTzszsxhQCGZNaPwA1f0mmf7L2Kbq8AEDoeWtIx3BEd_Gyn46_ZqD7JncfJtwUngdlw3m6xKcFuUOAuMjPBAFyLfF0iRrycnA_JNPXr-K6v1Fh-raLpM8sIJl-3Unlq_oeYAQw2Yzlzy6EUFj5gLf_-dVc0_FO1rNz6R2yQG5hFhjSWhymirZ1SMcf5NyrZxMgTIIsM85cQmCU7aYMwuIxujUqV2UhmA-dBBjDsIdIe3olne2Ek1h7nQy0KtYVRNJ_Emw9rLRDnpMNfmxXS16EL93lq5tll35Tfkg7fn6CvVatwzv6IfecrhbWbX0QVhJ_kKwbS6EIiViqa1eKzswlmBvMDUWF4cMO7FNyj4I3bD3IJKggnAC90sam9lTHGfr-0dBDE-yK5nRkrmdk9zdwYy6QLqLzlrnMRgTTi01EZ_Ju7-D0Ews0IaWlwFnSiGoHcBrgx30FZvGMxV_aSXXkQwmpNDiyrjZ--4qMN-VEKzT6egJnV7XliwDcq8B8OD-Zgb9Fzg1RNWU6AcmMwSm02CDU5aVBxxrBog7w6Pc7e8EYe5pCgdzO3jZECagNnKJPg__LonhOFghF13SortqhPTPopXN2Eog4thkUoCMUSQT800z69pwLPQagdBSCb6vbjJrqMC60KXZbaw_Wz4Xx66xZ3NNWCh6EhID-jJqDHzRYg.YiTKTpOnaRzUQ7wiijJ_hsl-N_uqI8eMJ-0rdPVLeMA',
        'refreshToken': 'dfa4b953d463ef8603b5d4debdc24afecab9701e42cbd121e0f277677a057cefced99166e579ecb6dd73091b61d265be9b6fd54006142ba814faec3fe708a75c',
        'retk': '',
    }

    
    response = post(
        'https://servicos.energisa.com.br/api/clientes/SegundaVia/Download',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    filename = 'conta_de_luz_082024.pdf'
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(response.status_code)


if __name__ == '__main__':
    # asyncio.run(playwright_access())
    baixar_pdf()
