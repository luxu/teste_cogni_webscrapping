from pprint import pp

from playwright.async_api import async_playwright
from requests import post, get

import asyncio


async def playwright_access(url):
    async with async_playwright() as p:
        url = 'https://servicos.energisa.com.br/login'
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        print(await page.title())
        await page.get_by_role("textbox").fill('20443596859')
        await page.pause()
        await browser.close()


def acessar_code_seguranca(code):
    cookies = {
        'CodEmpresa': '9',
        'MeuLocal': 'MeuEstadoExtenso=SÃ£o Paulo&MinhaCidade=PRESIDENTE PRUDENTE&MinhaCidadeID=1&MeuEstadoSigla=SP&MeuCodEmpresa=9',
        'primeiroAcesso': '1',
        'ak_bmsc': 'D271B498328C8215FC19A594DF0183F1~000000000000000000000000000000~YAAQpw8tF3+x+piRAQAAD/6inxhYukwJJtq8O0Fa/W5LZ4fl6YeZDbcMKsyDQPzJzVkn5bpfct82UeVqHa2njwpdP8Fus8IS5YTj0Kba8zaID5ATdHzhe+meYq7kjuZRpQj5OSk25leajsRJ0dgzGD2IJjFyUICes9tH4ELrDKg1tNPJ/9Wr1jHQRAFf+1S+J6K7IQDsPLWJJahe98MKNrrBWWroAFo2sQSDjWwphyITRldRlK60kOpuL2IZquvId2MEYQIa2Gh2P4non1eBKmSTDD+WaxQrG9o88Ouf5F5N8hF3aZuKW59ZlpT602WN1sIBNKj3uTJq5DVb/2jeOlpBvSeLvy7M8sfwFWQa7m0pV3u5Nj8S1iVqcfvHPV2ZWnBZaG2Z36RQxb1db54XvwevvJyJXytdWJY5yj/xUUKyh5HjpF7RntnQEBgVKsFdi8hRLmsDOSp6s8aQFqbipQmH0gmxLuYDyy8SY9byAVgkQFOxK5ElWlA=',
        '_abck': 'D9F64CE190DF5E6EFF404C5A1D786121~0~YAAQZw8tF3GRA5mRAQAApleonwx5kO9rOgZY48NRREgjwzkjHr51aEhbAN3iuOGvMqFFng/mua+e27IjP59xvbGeWtNRDUaAAqxm9uis7jU/PR3rVwbiNtiOxPg7eGsFcED1sQsa9Uo87y7mJ+WDUuHpnRlg4V7zAUK0dGm64DgLk+2tMmEdcR/rjwk1vwYPVRTAdp02FBhG/bQLatLDxehMyM2yYT0UhsyzGA+rqonCVspECp2w7JnX1FpkdXDpPh0LXdgdG4mGzzN/2F0yC4v2ugvPZZwqmMede7lecCEakSt3jZLAJhrCer5JAUSaHXyxqg8h0+zrVG2ZpC2nLWeyKb8+GuSw6MEXvJdmeKYvGMVzhEmp3LhWIXNgCWLsf1tcQ6gOrVgNF33ib9y2aZZLhkKZI893PDhf+d5hw4hBSYlEK+fBMpMzLZl1Bgf5XqjhRD12tFhAOXCWx/bg/Wuy89Jq8M+YAA==~-1~-1~-1',
        'bm_sz': '4E8A9516D5BCD427BC513C1061E1F5FA~YAAQZw8tF3ORA5mRAQAApleonxjmBnOqzUuBkzV7fV/rLLTF/Mz2gxyN5MPwzENaWHlVkeWgNbU4w9U/BoVttC89cA8cs8NPM5CAVmjhabcHSYB163iV7sVDn7NY78my8ztN4IlkJfKbODG8WEDd5kgeMj4EMbI2G7C5O2FH3kfzYPnLZ/T62H87daDReN+hn8g2wdLDbqkO1h6vDXUNeZZoV/UvagKGSgdI5SGSWN+78Q72itpMx5xn16JUA8woAQXaEi9x6iFgpMh4RtCA/hSfqAJunULVPancTS1eDKZPCMnzJkWbnkU0WzbE8/ENQyq+7NgG9dgxCFeybtgKxcmPvbVqzPSfwa41AgMtYKkDmcgTbk2CWZlil4ni9AdpxRsqEzIc98AoQZ8udYhBuUq9A1MmGIq6If7gSMC2/bnf6Kg1D0CMm0VYppGehbqb62OMtkPc568wCOWU6JNxRU4=~4535609~4274497',
        'LF3fHRAjveUqny8PdrxipHkZPYh69DqgJ8tkoB6p': 'Fe26.2*2*f5437168e705dd4758f20e180da97213d42ffd2481ccec8b596197ea25589ce4*LxCahuZGWfu9PdjMsg6oqA*D06CtmKpRziyevHzlv9UOk-Cz-hDdD4hyYV6nGsU2uXMKrJ2oipMF3MWNKJQxLoQiq-4lKv_Xau57YlwzdT2tACLTk25abzOulmBjtebegdg061A4tTHiW56naf7PD-QOIOPak5vsKCoKYMvjvIQkQeQhS5xS-k_VYuKZ7w3mho*1726256495603*cc2dbf84cddd86939f934c6cf5dbc59e21e67507898eb5409abcf3bf151fc0a2*dYgItWtC5J5q8Jrmq8xhVeicPCfEtEbUsSHbsbkZANo',
        'bm_sv': '6BFEA3CD7C7F57FF65483FB87717B04D~YAAQpw8tFxld+5iRAQAA/d+unxjtKrCEdilbAIcGrnbubuRDhv36PDArZHLoYN8Evlm8TmMCNBs8KLMg7CUTSll1xTG/0T/lrFNdhkaDogH18CFqCd8DHfHdhJx34p1tR8bnH7vu56WirKktPBdoog2TS1ql0JZgqEoYRezO4IN3J6yY6Iw9d9wPG3kvr+vEzMBzSrL3p+tJfuiENpIMe7o6PWVWZp5Sg1Srp1ewLy+UHIVUMa89b0OfmGJ7V3ET9+w2UQE=~1',
        '_dd_s': 'rum=0&expire=1724962045998',
    }
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'pt-BR,pt;q=0.9',
        'content-type': 'application/json',
        # 'cookie': 'CodEmpresa=9; MeuLocal=MeuEstadoExtenso=SÃ£o Paulo&MinhaCidade=PRESIDENTE PRUDENTE&MinhaCidadeID=1&MeuEstadoSigla=SP&MeuCodEmpresa=9; primeiroAcesso=1; ak_bmsc=D271B498328C8215FC19A594DF0183F1~000000000000000000000000000000~YAAQpw8tF3+x+piRAQAAD/6inxhYukwJJtq8O0Fa/W5LZ4fl6YeZDbcMKsyDQPzJzVkn5bpfct82UeVqHa2njwpdP8Fus8IS5YTj0Kba8zaID5ATdHzhe+meYq7kjuZRpQj5OSk25leajsRJ0dgzGD2IJjFyUICes9tH4ELrDKg1tNPJ/9Wr1jHQRAFf+1S+J6K7IQDsPLWJJahe98MKNrrBWWroAFo2sQSDjWwphyITRldRlK60kOpuL2IZquvId2MEYQIa2Gh2P4non1eBKmSTDD+WaxQrG9o88Ouf5F5N8hF3aZuKW59ZlpT602WN1sIBNKj3uTJq5DVb/2jeOlpBvSeLvy7M8sfwFWQa7m0pV3u5Nj8S1iVqcfvHPV2ZWnBZaG2Z36RQxb1db54XvwevvJyJXytdWJY5yj/xUUKyh5HjpF7RntnQEBgVKsFdi8hRLmsDOSp6s8aQFqbipQmH0gmxLuYDyy8SY9byAVgkQFOxK5ElWlA=; _abck=D9F64CE190DF5E6EFF404C5A1D786121~0~YAAQZw8tF3GRA5mRAQAApleonwx5kO9rOgZY48NRREgjwzkjHr51aEhbAN3iuOGvMqFFng/mua+e27IjP59xvbGeWtNRDUaAAqxm9uis7jU/PR3rVwbiNtiOxPg7eGsFcED1sQsa9Uo87y7mJ+WDUuHpnRlg4V7zAUK0dGm64DgLk+2tMmEdcR/rjwk1vwYPVRTAdp02FBhG/bQLatLDxehMyM2yYT0UhsyzGA+rqonCVspECp2w7JnX1FpkdXDpPh0LXdgdG4mGzzN/2F0yC4v2ugvPZZwqmMede7lecCEakSt3jZLAJhrCer5JAUSaHXyxqg8h0+zrVG2ZpC2nLWeyKb8+GuSw6MEXvJdmeKYvGMVzhEmp3LhWIXNgCWLsf1tcQ6gOrVgNF33ib9y2aZZLhkKZI893PDhf+d5hw4hBSYlEK+fBMpMzLZl1Bgf5XqjhRD12tFhAOXCWx/bg/Wuy89Jq8M+YAA==~-1~-1~-1; bm_sz=4E8A9516D5BCD427BC513C1061E1F5FA~YAAQZw8tF3ORA5mRAQAApleonxjmBnOqzUuBkzV7fV/rLLTF/Mz2gxyN5MPwzENaWHlVkeWgNbU4w9U/BoVttC89cA8cs8NPM5CAVmjhabcHSYB163iV7sVDn7NY78my8ztN4IlkJfKbODG8WEDd5kgeMj4EMbI2G7C5O2FH3kfzYPnLZ/T62H87daDReN+hn8g2wdLDbqkO1h6vDXUNeZZoV/UvagKGSgdI5SGSWN+78Q72itpMx5xn16JUA8woAQXaEi9x6iFgpMh4RtCA/hSfqAJunULVPancTS1eDKZPCMnzJkWbnkU0WzbE8/ENQyq+7NgG9dgxCFeybtgKxcmPvbVqzPSfwa41AgMtYKkDmcgTbk2CWZlil4ni9AdpxRsqEzIc98AoQZ8udYhBuUq9A1MmGIq6If7gSMC2/bnf6Kg1D0CMm0VYppGehbqb62OMtkPc568wCOWU6JNxRU4=~4535609~4274497; LF3fHRAjveUqny8PdrxipHkZPYh69DqgJ8tkoB6p=Fe26.2*2*f5437168e705dd4758f20e180da97213d42ffd2481ccec8b596197ea25589ce4*LxCahuZGWfu9PdjMsg6oqA*D06CtmKpRziyevHzlv9UOk-Cz-hDdD4hyYV6nGsU2uXMKrJ2oipMF3MWNKJQxLoQiq-4lKv_Xau57YlwzdT2tACLTk25abzOulmBjtebegdg061A4tTHiW56naf7PD-QOIOPak5vsKCoKYMvjvIQkQeQhS5xS-k_VYuKZ7w3mho*1726256495603*cc2dbf84cddd86939f934c6cf5dbc59e21e67507898eb5409abcf3bf151fc0a2*dYgItWtC5J5q8Jrmq8xhVeicPCfEtEbUsSHbsbkZANo; bm_sv=6BFEA3CD7C7F57FF65483FB87717B04D~YAAQpw8tFxld+5iRAQAA/d+unxjtKrCEdilbAIcGrnbubuRDhv36PDArZHLoYN8Evlm8TmMCNBs8KLMg7CUTSll1xTG/0T/lrFNdhkaDogH18CFqCd8DHfHdhJx34p1tR8bnH7vu56WirKktPBdoog2TS1ql0JZgqEoYRezO4IN3J6yY6Iw9d9wPG3kvr+vEzMBzSrL3p+tJfuiENpIMe7o6PWVWZp5Sg1Srp1ewLy+UHIVUMa89b0OfmGJ7V3ET9+w2UQE=~1; _dd_s=rum=0&expire=1724962045998',
        'ispublic': '1',
        'origin': 'https://servicos.energisa.com.br',
        'priority': 'u=1, i',
        'referer': 'https://servicos.energisa.com.br/login/codigo-acesso',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }
    params = {
        'doc': '20443596859',
        'codigoSegurancaRecebido': f'{code}',
    }
    json_data = {
        'ate': 'eyJhbGciOiJBMjU2S1ciLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwidHlwIjoiSldUIiwiY3R5IjoiSldUIn0.xdikPswHOBah81Kl_Se9x3MghTdy8IY-YE0g0hVbgx0XGNdYHFqpYGF5KGCxPN0SbW8Hb2KmFvRUZPDaWYvWWd1LP9JF_Kam.FoaVY74a9RZYjZoM_rHg7A.u6GX_8vGuLT-odZuHTtkfrEUifl_vQhJVInFHucFeHucZsTnY7fRKNs1gE2L8bpJTWAPs-dgGYeQKp6ieOa5qYddtCROTeaaupLaK0bCl8sdOpGrSPYoHVw5sGgu7oRaWpsVeLOE-iFGPBuNSJDuOGqCi5KLf4_3jN4004_h72OKoWf_9JJx-1AgKBn2qF6m-ouxTM0SZP4cHrHzMkFsXXkCAKuXWhlKpaEf6BlrOhDE86oFdJgP7b70JKFkA_OlMe2OCiccX5P6eF7Sg0iqQl_xufl3d2jGuiky8gAdR1dhTCZsv-dtnfiMBQJLhbSoQm_WFxtkPjASNi30uQwBk0c64ORF8ESlRbyd4wGvE3yDGPX1K6p5toqn-YCx3ayFUxHQT9zMLfILk4k6UbyB_1DYh6jHGS73AwXDi6AOdwkDCyqPUaVRUefLX9ihRCfeBc2INXv5_1gmehfgUSVHrofGdSEEfNfjPGxxzBwkJd55LYnwsXLumybcVXAztSQdo2hu5O75N2mqK6YhI5sPXVnA29-z0PRc8crTPeue8h2-mRGJwc2QTViBmYSRec7K0sg0VtJrZ2AWXDzPdTZT3HNYbo3ot7RN7GDMYIf7WlCf8TlRRQNG8m4u1nWtVMrcdGh4EZ5GsuewgkfKvuDu_c1z1a-Kf6kIy7DkhQnKwWVRqTImXperEQ3T6iwlVUlRHIG-urWCBe2W1DB_0iDHLTcR-4RAgeioMo2nD_fNFKSoImefzhEtK1CxfQEbcIYRUw3cuQcID_UzHKlyqHkqbKBwBstFIaNZ2c-ZX9jJBqGOr1J_jnqlklKu8yi338cjm9OGi5nl__tdQSicWYx2fO1tZ0vGqs4p8atHLPtqwqxneMGnr2WnhTj3ZLLwE5oh_0MEBKJ1FZwVEKsFH6X2FF9dhmOXmq1uQCs9uHjD4QziNuQ_Qv7v3CjBkGLQan8JaOn3EwHsttEoTeoMn8ZMC6AYgemomJxOnlsctSmzhYnHq9yuUvmHIo96KARabjeK.ipSg3_kxe0dPieBTjfWja7Va_sOFXqvzZnWvboA7AO8',
        'udk': '',
        'utk': '',
        'refreshToken': '',
        'retk': '',
    }
    url = 'https://servicos.energisa.com.br/api/autenticacao/UsuarioClienteEnergisa/Autenticacao/PorCpfCnpj'
    response = post(
        url,
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print(response.text)


def consultar_infos_cpf():
    url = 'https://servicos.energisa.com.br/api/usuarios/UsuarioCache'
    cookies = {
        '_gid': 'GA1.3.961648134.1725013507',
        '_fbp': 'fb.2.1725013507716.977698556218039783',
        '_clck': '1oev70y%7C2%7Cfor%7C0%7C1703',
        'LF3fHRAjveUqny8PdrxipHkZPYh69DqgJ8tkoB6p': 'Fe26.2*2*36c8b74627918e079f102f44952ef89b1f707d75ed21f25136f3a9ffefb78574*aj5IygGRTGbjg70xLmdb3A*EVBx64tOWoND2j6e6tnp8_CV-Nck8w27Ur3FLiO2-BCp2GqmWjq-RaKET762qXYIX2k-pWWKgHDvIrpK0BA41IF9xJRgsOT5SnY-ZyNX_tqXSs527EEn-OG8jsk22B9IH98c5FqLZxCdH0dzFzQSKvF2zrdPLnFacRjTzRrzdio*1726309560148*265e22786bfcd2826c333e267b8d29b5dd8631007d1a3451ba3daf6fa35e7474*nvc1IE5_xZgXhUU5cDHJH1Zy8sVzRi04OZ2E6xBg8As',
        'bm_sz': '4A886948B0E8FA72C847942607FEF8C7~YAAQpw8tF81YFpmRAQAA9jygoxh1GpqkX59ShA1faL41XXWqCsTUpSHjZ3oKxI5teh4+qhK59vA7/MSG39b6W3PrEBUhq/EnUjqolnZGm8YPY0KFGrCtEK0dFfRBp4LryGLC5+XmpRYiHVj84AbD758WqWMWSvgJTQN13j2Sxh9q0OSYb5YzqD3A7s9WlHbP+lpyqBlG7DfIF1MK8oCGN+Yp2Eax7dU+VoPShCHcjtX2vOa3EuerClpSSuDEj/irMyPNUJJknj42YzV/3SslPmivcj1FDjXbIEXFooRtULVabCeznkBsb6lEwgc0ehbzbY6u/TCyvrWiu2OEW8AtCKJ9xGvHeMf46ifrshxQ4OjS24hjXGz8w9LgtqnhQ7qssZPfrsiTvBuTb2+kJOlHhZlOuDHLr4abiEor7IUWQ2TqOPr/baOzCcXcclp/Tk+0NuqSI1DG0ReNHosiBXK4PicTfEZ6OqlP066js4NKOvfb~3616834~4404791',
        'bm_mi': '7EC6B9A69164CE7D3CE7B818A2E1BEBA~YAAQpw8tF41ZFpmRAQAAEFigoxi3trffIO3F6+vhpao6B7jpXj3WJoTLiAtxGWoYahXtiAXJj20Tv2+3AMQZbOCagecUFf6zcjjGuhBVwPBOAidr+kRizexFKfJR2gO22V1BQRJnWYbw4/Y3S+LYCrpaPKk0A13He/Rk28ScYhdN3SmIqRLcuY4EgeINm3NI0FK1NAX0y/dcoELpdJl+V3ZfwjDReyl/rtbPkvvAVvGPtJKeJ2m7BsVMJl9IWHvgBeXv3oeLk7hdokjNq71gTVBW8vm4GO0qgviSPCtdBtrZwefh9qjkTrYwKGj64hSI~1',
        '_ga_X3RN62760T': 'GS1.3.1725027072.1.0.1725027072.60.0.0',
        '_ga_JT7VJSPDK5': 'GS1.3.1725027072.1.1.1725027072.60.0.0',
        'ak_bmsc': '48A48FCC2E5943C33E2B8190CD28F5B4~000000000000000000000000000000~YAAQpw8tF6RZFpmRAQAAJV2goxiw8rj0aEZKzRLgtbf8WgJjaiH6leIxXW+8cg5YaL51AtRv2dp35BHQX1H1geQFoONozjDitZc4HvZ27lGXvRIeYhm5LFCXuP6Vs08ABfiaw/sffJ4GySgcI/sd+yuTFI0KyDfdoYUNxy3l439MOkLVlz7QdYA38xAueV7xiKWTYGc1dOe0QGh9777n0vbQV0VvsHQWD0P/vwEz7xbu3mJIvnJZBrJ4RXlS+MgL634Sm29+8kfzvUinBWfPDEtbwP3Jdi4VVXUNaggDNZuQCCOmwAKdtytca9fGLh6VMts4yWA+d6CLANN9qwQY/2AvfjyzbUakyZSmMBTMODqQGYpG1nKijszYaeT4XLy/HBXy7rtVanovUddllzw/6zXwWsLmWwA8zTkDI48304+AuRRcBvYR4G2qU+x5WOdiVJlQ4YpFddV2ZZzcHyaPu/qgmCx08sMVn8g0eWhgcVAiTh3HVf4TobXl2ozDY9w7v+IFkxLCbGhySA==',
        'bm_sv': '35D988846D873B6D0992EE479C197990~YAAQJthJFwQjlpuRAQAAX1C7oxipW71azG9qdgppJeTDwJR1fLBT3si/WFOZN2EpuKhXQL6Hu9MlPmjLXInlha3ymflbSF9Sq1M5tmg9kpfFo9CpBtHpTyzYnyU3QUrCBUS9PlN8PBayZz+lt7vH8k0kc7+bpG0j3oQCVXmYa0wtjLbuhyLvYU0J7sTzJLgu3PS5CO5tPcc2EIg/U3FGEgjDEhWc6fo5LJd/svOWMTBBH1Q2cRe/4fiXD8MXazwbN8fNcZ4=~1',
        '_abck': '2D47FEF8F94F4ECA6AC46EEBC1277DE6~0~YAAQJthJF84ulpuRAQAA4W+7owxAAMfw1iquWI7jIwTMM41iOfZJYd9zxrwjN8th1/8RMVPZPLd8uRjCSSB45sNRFV79NSyVdNVV56/nwu2fnYyqJ1I9uvR59qZ54Gxjf6VKoRzAuDG5LzSR0/HiaA26nmM8fW7RGP1NdghhRwZRjEmibRnFjwH1PPHC4DBXfBwtmFCxd1ctRWZu7Wjp+seOEYX3MBgJr7NUE20rhdV40gbe3MRDCv7ByZsdLFW2e6AYNEn4nADXEa0Al1/wwQH/bI/teEOXSZ4zQpihXoxZjVrFINRiL/8gBon/IT8Vt+L71GWhm8aFqXKW04stjSOqvHM9Dnf0jUIZZ9J6IVM+qHXEim591ZiM5u6B2+bsGMo6fu4dLJLfB+kgcrka302WMShGvRWsq8raPYToa1k+IlY1Q9Qb1PwwmhwsIuTLkk+rUeJLPU8/s2vCW0ajO41hLro87D9NkrzEUDXYcSiD42PEuLT889MpmqTuUXDOHA/ZPhwAhBkkftNM16HhH9QSuwMo+UtoAFI6xjKpGjNlJAtbzO4mVUJcj6Q=~-1~-1~-1',
        '_ga': 'GA1.1.451642.1725013507',
        '_ga_WMNSR52TVF': 'GS1.1.1725027065.2.1.1725028847.0.0.0',
        '_clsk': 's0gn2s%7C1725028847819%7C7%7C1%7Cz.clarity.ms%2Fcollect',
        '_dd_s': 'rum=2&id=19453571-a65e-4725-8ad6-c7adaee3cfac&created=1725028809818&expire=1725030076006',
    }
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'pt-BR,pt;q=0.9',
        'content-type': 'application/json',
        # 'cookie': 'CodEmpresa=9; MeuLocal=MeuEstadoExtenso=SÃ£o Paulo&MinhaCidade=PRESIDENTE PRUDENTE&MinhaCidadeID=1&MeuEstadoSigla=SP&MeuCodEmpresa=9; primeiroAcesso=1; _abck=D9F64CE190DF5E6EFF404C5A1D786121~0~YAAQpw8tF76s+piRAQAA/siinwzbjG5p6VfP+LCnDEOyUy9gZ5VutoguL8076X8KR4gTQD0coKhk1OFKDt5e0HlOKuuuNNqaMB7bLu3lpZTUzo2+UL6CKvDKQ/JdAFHxLSrpJ4hO6FatNZKnkHkjnhLA6ziPuJkB3/hXRS0gfoNPvPN2xW5lXNvVQnaOo+i6DVqbGqvRVsXeXsXPiddGMko79JIOm+d9RhlK+8zwNRSbQjWiTgnkJtCQVuoaBIGCLT2RT8wvTEnv0Lth7yaMUNxqbWpDs2aquZPgDosJuRQHdNGyQ8SnWtFF5NKPYoLs6lUuLIPAj4yS3MDrnhIb+g/6osasGxFaKYA7ANhGoFfdCby4HbR2kolu12G6u0r/QXsdcWndD1UP/GWb6WHck2t0SiABu2eu9vN5dS9AAMHBs6z1kTLT0Ci5a2XbXVtAnfiiYlOlVtBbs8m2PzsL+suwgbSQP+G7hQ==~-1~-1~-1; LF3fHRAjveUqny8PdrxipHkZPYh69DqgJ8tkoB6p=Fe26.2*2*75f168477bb3c4237b1909a92d3c78190fb9786b2f0b216d8e242f22fd091c6c*yO--Uc0mz1UOyezMBzlBJA*-aDJSahYUGbBXFwGLRAZr-UIRSSFH8OCp99WbKlb92kjz1NrtSHJ3WltPF7w1a6kuWcDrhRFThKLjLF_9HHxG-6pACwUvcn2pHRYoPKAfAlBhZIL7QRk7MMyJNaJuFkDXBKljsW-zFAyXiPYK805GxoGBMBP66AkYTknFyYhuuM*1726256133165*f251ddb81235f49c302bbe9118a7116e8ced8d02b77b8f7d80a060f72b6a1ce0*5Zm6CJLc07rOcf0NG7_47QCx0jCl0Z3mUrhLJIrNXvY; ak_bmsc=D271B498328C8215FC19A594DF0183F1~000000000000000000000000000000~YAAQpw8tF3+x+piRAQAAD/6inxhYukwJJtq8O0Fa/W5LZ4fl6YeZDbcMKsyDQPzJzVkn5bpfct82UeVqHa2njwpdP8Fus8IS5YTj0Kba8zaID5ATdHzhe+meYq7kjuZRpQj5OSk25leajsRJ0dgzGD2IJjFyUICes9tH4ELrDKg1tNPJ/9Wr1jHQRAFf+1S+J6K7IQDsPLWJJahe98MKNrrBWWroAFo2sQSDjWwphyITRldRlK60kOpuL2IZquvId2MEYQIa2Gh2P4non1eBKmSTDD+WaxQrG9o88Ouf5F5N8hF3aZuKW59ZlpT602WN1sIBNKj3uTJq5DVb/2jeOlpBvSeLvy7M8sfwFWQa7m0pV3u5Nj8S1iVqcfvHPV2ZWnBZaG2Z36RQxb1db54XvwevvJyJXytdWJY5yj/xUUKyh5HjpF7RntnQEBgVKsFdi8hRLmsDOSp6s8aQFqbipQmH0gmxLuYDyy8SY9byAVgkQFOxK5ElWlA=; bm_sv=6BFEA3CD7C7F57FF65483FB87717B04D~YAAQZw8tF9uIA5mRAQAAUdunnxiyPdEzkjYeV6Pshqv40H0r5o67OR5TrKBSvNfhpYQAIvis+tyMupIQyIwf+Zr35OOOjqIaxNPcRnL09+Ld0X+ixI7ExB3T8o3b7uiDWqpKYd5GwCskFeW32c0CF2ZDHGp7k4LD6gFW/7+g7uaJFwGothaB13FErvhbTYzE8eipqd1JkOb89czFkgSz/e8/oLNjko3U3cNG5b2oHdUOvuchu8v79K1lxFCq/K2tLP/9F+0=~1; bm_sz=4E8A9516D5BCD427BC513C1061E1F5FA~YAAQZw8tF9yIA5mRAQAAUdunnxiragDBafnYme0w4NtbOlh/fC1MoUSIewtK8dVDy4dRfi417NyThqUiLgzhnSTRjVsTLemJhCHiksDd6b5aqSCVymTH1wnUieFFE8UpaEzQRasUXsEwWdr3XKZGnvtaezw4epHRKRSkSz0volgSZPKsTFrhQVXI7RVB0oZ3mTRSyq/dQy+kAdVGwyLvryggr1M6DAGO6DJfc/zEFFUF3OTEKlK2FfDqrUeB+k7eXSlW8rAqxc2S4Qs2UkJwZ8/YJAhNR78NvI8BBNwbibpwDCLR10CpUv4Qs5N6wrmjhFmZgtWf5X8O/2SRjihrPuhwNRBmebgnwD47C5N5U29LxTeXF0CJCZcP2w+kfoOXwoNkexYMkiNDqcy9Eod5+FUv8jzLDvLego9vHW9THt/FW7vB3Tag/iZVpaWQm6wkYerLVoF7toCQ+Mo=~4535609~4274497; _dd_s=rum=0&expire=1724961384607',
        'ispublic': '1',
        'origin': 'https://servicos.energisa.com.br',
        'priority': 'u=1, i',
        'referer': 'https://servicos.energisa.com.br/login',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }
    json_data = {
        'ate': 'eyJhbGciOiJBMjU2S1ciLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwidHlwIjoiSldUIiwiY3R5IjoiSldUIn0.0UDBAp3gfe-RVakEa91t0RqG4eYRuqDuyBlNCLy-zD0fGfn23xHTwL7F4rcxaC6O9HDQglAjhEF6QKB22XsMZxrWGClr4ONn.nDgk9xg7QJD1_7LnP_QBrw.gwphyeFZ7Lg88dFcJxZMHbC4JWgShcRjL-bNkgqSv7AmEvd3XePKigBZ9oGB0j2gF_9TKGhWTVshDgVyHAqb_Gg9zFVc7Sgto0nvC27vPnONh2LlesS4aR0sueaL7Hfsbw9ezrPZmjqSOuPtnqvOySmaMZ7q95fwB8vwd0WxE-opUpjnIeZcRfBE3HwkC02i6hw6saJDYqVmdB0dOIrwIOKcm3CeF8h_q0X9DuN2lwzxumVm3RhadboakKWYfgsWEEiGstwMzEqPjV6Smqhfx1kz6gh68vsSYp9Xhv0cRDVn8JvJx6dbS4ovbTw24zKTYdgRidMGBX6Wl7-QfrEgDxCBJHv84f6KBFj7onM2SjvrdmwCCozWdm-LOopiJEwIWGFyBaE9xqlslYA6syuvIH8KAy8wUF3HlK70WnT3M_-uI0ZWOVCOUPNcNcZWjde-W1xnfq_46ET_17fpxpY3RRbaXMnvHBn2shHiNtjJR5_J7ZJsOm-65jLfhB5dmrhDBzmE2MtaFlmfeVH9POXa0pIFE2CPJSRZ5mlbcR47QECDvaAxZ7seu9sBySGXruVGpMKEdBe7O4hCs8pDSkHusYUD4ZSUdIcvLh-PGU9TxgbpOTl5JRjHDOaMEP-w2tYV_0lAEMfgvNtC_sRso3oajVnXV1GY-Sl_ScuZ-xXHrf1CYVQV01zcW-5vt1gEd3wtHncZRlNRtGz0pqsnnMNoUVSCdK6oWYZWrsCxrhpARtk8HLr8FjkpkVbPGcmOB_-eQxJcad7ODBtx0hazjYOtdqOS9chTWwsc532qoU1AR64HLv5d1NgD6_wPWH_OfQtpdc_LLxKNC2oz_jcDyLnO88GNkx4IJs7_rTeCWm4dbbW56V-nMrSr7L08yFnu8IuX6zhdQLVJe8mwW1OsjHjmffI2XxH3P-wxPDndjEpk_uPQ8MpPhHxhF-R22NK0sblZXcrlCA-TDPJkITkMduZut08SxSkkRKtmALaaGy9VV_6zaJpVJMSOiYQSnGZ9T3he.AN-fCx0Indnw8tmEGAlErs_XkGRVMwQiqeMOba0LYVo',
        'udk': '',
        'utk': '',
        'refreshToken': '',
        'retk': '',
    }
    params = {
        'doc': '20443596859',
    }
    response = post(url, headers=headers, cookies=cookies, params=params, json=json_data)
    pp(response.text)

def baixar_pdf():
    cookies = {
        'CodEmpresa': '9',
        'MeuLocal': 'MeuEstadoExtenso=SÃ£o Paulo&MinhaCidade=PRESIDENTE PRUDENTE&MinhaCidadeID=1&MeuEstadoSigla=SP&MeuCodEmpresa=9',
        'primeiroAcesso': '1',
        'ak_bmsc': 'D271B498328C8215FC19A594DF0183F1~000000000000000000000000000000~YAAQpw8tF3+x+piRAQAAD/6inxhYukwJJtq8O0Fa/W5LZ4fl6YeZDbcMKsyDQPzJzVkn5bpfct82UeVqHa2njwpdP8Fus8IS5YTj0Kba8zaID5ATdHzhe+meYq7kjuZRpQj5OSk25leajsRJ0dgzGD2IJjFyUICes9tH4ELrDKg1tNPJ/9Wr1jHQRAFf+1S+J6K7IQDsPLWJJahe98MKNrrBWWroAFo2sQSDjWwphyITRldRlK60kOpuL2IZquvId2MEYQIa2Gh2P4non1eBKmSTDD+WaxQrG9o88Ouf5F5N8hF3aZuKW59ZlpT602WN1sIBNKj3uTJq5DVb/2jeOlpBvSeLvy7M8sfwFWQa7m0pV3u5Nj8S1iVqcfvHPV2ZWnBZaG2Z36RQxb1db54XvwevvJyJXytdWJY5yj/xUUKyh5HjpF7RntnQEBgVKsFdi8hRLmsDOSp6s8aQFqbipQmH0gmxLuYDyy8SY9byAVgkQFOxK5ElWlA=',
        'LF3fHRAjveUqny8PdrxipHkZPYh69DqgJ8tkoB6p': 'Fe26.2*2*8248ce5aa38cd1fa68fe9729c2fb49da0401eee467e302794ceba0888178df26*4kKoZKHPsELYI-TJ2uuu2w*JCnbIF-7r4kriuyL-iR3hxDS_hqwxOeh9Uidf-Kzy0Zdt846S29JaVO4aGsgxaCSng58ohUkGG07shTkkZeqjWGorCju4sGDydksxotCmDLE7G6xYSuE4sLLV16whY_ZSNgCSp0wcP4HqP0ferPxE8onFLJMEOA3tNzemAOh6RE*1726257379641*03a217ee63ea102adbcbeaa28318adaca22b73d4534ef471c3e2ce2836292e32*V-BAMGEE5xgnoJz7OCsNsPRvz-yt5huyFKQp79Qx3TQ',
        '_abck': 'D9F64CE190DF5E6EFF404C5A1D786121~0~YAAQZw8tF/14BJmRAQAArne2nwzc4enI4Bb95MyYbEtCwoELICKc2EtQyRqwfgbpsw24z5Id+ZuYIntmHYngHHl80tz8+UxfgqnKcDA+WrVmYTDpLPl+E5FukiUtM14+xzdlwq36mziVThknnJzP9junV8O93Q1WCYwnNUypEI8RuuhL/WQCHY4Ndc8j+1G7uztTZ040qfBO8eVg918K7EXHhvobEFFgzXCMySlGjZPSuV+7c+/jnOyzX36556Ut/Q5pGi8Z0Uw0fWnR3AQvK1Ram/CXogbHtfmRbNSlYhkfCKxurk7x75AFrjH0BY4Bw/u16p0qh1SISCfv7iQLaO94LukNCIYpsaCkW+iRVGijW2c3mAmLnbCv5iKzmv8ssm3hJWir7uGkShF9uRs1z0jrmv0h0OLYz4hHgXFTJt98vu+fM0+yXnkcxQ6GjluSI4X45y9NSolsFaI9RJaEdTpATSB5OGxsQQ==~-1~||-1||~-1',
        'bm_sz': '4E8A9516D5BCD427BC513C1061E1F5FA~YAAQZw8tF8emBJmRAQAAZfC4nxiMCmzliXgqbB8oI6gFWXeWnA9LDyWxGg7FnO74sLEdhyqxpZXYprI3c6M+jCeizJbNI9OoLbTkgqFDDooNQz3e2vF8u/4gjy80bxU5IIeFcv3ny3h5QZ5SkN+MTLYSbLAi+5qj3i8oCSxgy4U9MrpdSiPG6nT8AOac0OiWIyUpzpX8bU4YBZdCaa5bhtuYGlRrpEF7nyxxGHrIQPCCt/rp6+l1iLDE2sgM7GYBMO8zJnwtjbAY6x3OCYYnWc3ax8nAn4gG4JZy9+NOzDEP0nbTlXAfFBB756oEkjMXN7iat+lz0oMjqfe/x6BXXGyRpnLchFlELshGAu2zJ/H+zFR8W5aeuvONm/a38SJLW8Rs0wS7EnDW5P5/4WZ5I2tTemM71gyU0ck9FaIW7lOG1t/V4wwBl4op9OoQV4O0bEOhxw5aXR3Hl2WQM6YzStSNlvcOZjfFT/H/WVTRzhk=~4535609~4274497',
        'bm_sv': '6BFEA3CD7C7F57FF65483FB87717B04D~YAAQZw8tF0ynBJmRAQAAh/i4nxgmy/Xp7QzIJ1s/19RelwG7Buvc+EE2ZcbUuX1XFYe7Q4MZ0TV1vvARG/vBvk+98tSVK7+vxQT9spzpvS36RvwJ+rmTI6OJObEEPznRbeXn7DscN380dJIfWcr1uKGOKNX8jm+FPJOzM6REr1cf7vnfPFfctaxdFKOkxA8BgIeifYZL7QDcMbLRhSu18iEu7dvhiEUfYQFtHXrI9Pr6THKNQumBk/M0a9Pl7iKSvDRsWYal~1',
        '_dd_s': 'rum=0&expire=1724962662716',
    }
    headers = {
        'accept': 'application/pdf',
        'accept-language': 'pt-BR,pt;q=0.9',
        'content-type': 'application/json',
        # 'cookie': 'CodEmpresa=9; MeuLocal=MeuEstadoExtenso=SÃ£o Paulo&MinhaCidade=PRESIDENTE PRUDENTE&MinhaCidadeID=1&MeuEstadoSigla=SP&MeuCodEmpresa=9; primeiroAcesso=1; ak_bmsc=D271B498328C8215FC19A594DF0183F1~000000000000000000000000000000~YAAQpw8tF3+x+piRAQAAD/6inxhYukwJJtq8O0Fa/W5LZ4fl6YeZDbcMKsyDQPzJzVkn5bpfct82UeVqHa2njwpdP8Fus8IS5YTj0Kba8zaID5ATdHzhe+meYq7kjuZRpQj5OSk25leajsRJ0dgzGD2IJjFyUICes9tH4ELrDKg1tNPJ/9Wr1jHQRAFf+1S+J6K7IQDsPLWJJahe98MKNrrBWWroAFo2sQSDjWwphyITRldRlK60kOpuL2IZquvId2MEYQIa2Gh2P4non1eBKmSTDD+WaxQrG9o88Ouf5F5N8hF3aZuKW59ZlpT602WN1sIBNKj3uTJq5DVb/2jeOlpBvSeLvy7M8sfwFWQa7m0pV3u5Nj8S1iVqcfvHPV2ZWnBZaG2Z36RQxb1db54XvwevvJyJXytdWJY5yj/xUUKyh5HjpF7RntnQEBgVKsFdi8hRLmsDOSp6s8aQFqbipQmH0gmxLuYDyy8SY9byAVgkQFOxK5ElWlA=; LF3fHRAjveUqny8PdrxipHkZPYh69DqgJ8tkoB6p=Fe26.2*2*8248ce5aa38cd1fa68fe9729c2fb49da0401eee467e302794ceba0888178df26*4kKoZKHPsELYI-TJ2uuu2w*JCnbIF-7r4kriuyL-iR3hxDS_hqwxOeh9Uidf-Kzy0Zdt846S29JaVO4aGsgxaCSng58ohUkGG07shTkkZeqjWGorCju4sGDydksxotCmDLE7G6xYSuE4sLLV16whY_ZSNgCSp0wcP4HqP0ferPxE8onFLJMEOA3tNzemAOh6RE*1726257379641*03a217ee63ea102adbcbeaa28318adaca22b73d4534ef471c3e2ce2836292e32*V-BAMGEE5xgnoJz7OCsNsPRvz-yt5huyFKQp79Qx3TQ; _abck=D9F64CE190DF5E6EFF404C5A1D786121~0~YAAQZw8tF/14BJmRAQAArne2nwzc4enI4Bb95MyYbEtCwoELICKc2EtQyRqwfgbpsw24z5Id+ZuYIntmHYngHHl80tz8+UxfgqnKcDA+WrVmYTDpLPl+E5FukiUtM14+xzdlwq36mziVThknnJzP9junV8O93Q1WCYwnNUypEI8RuuhL/WQCHY4Ndc8j+1G7uztTZ040qfBO8eVg918K7EXHhvobEFFgzXCMySlGjZPSuV+7c+/jnOyzX36556Ut/Q5pGi8Z0Uw0fWnR3AQvK1Ram/CXogbHtfmRbNSlYhkfCKxurk7x75AFrjH0BY4Bw/u16p0qh1SISCfv7iQLaO94LukNCIYpsaCkW+iRVGijW2c3mAmLnbCv5iKzmv8ssm3hJWir7uGkShF9uRs1z0jrmv0h0OLYz4hHgXFTJt98vu+fM0+yXnkcxQ6GjluSI4X45y9NSolsFaI9RJaEdTpATSB5OGxsQQ==~-1~||-1||~-1; bm_sz=4E8A9516D5BCD427BC513C1061E1F5FA~YAAQZw8tF8emBJmRAQAAZfC4nxiMCmzliXgqbB8oI6gFWXeWnA9LDyWxGg7FnO74sLEdhyqxpZXYprI3c6M+jCeizJbNI9OoLbTkgqFDDooNQz3e2vF8u/4gjy80bxU5IIeFcv3ny3h5QZ5SkN+MTLYSbLAi+5qj3i8oCSxgy4U9MrpdSiPG6nT8AOac0OiWIyUpzpX8bU4YBZdCaa5bhtuYGlRrpEF7nyxxGHrIQPCCt/rp6+l1iLDE2sgM7GYBMO8zJnwtjbAY6x3OCYYnWc3ax8nAn4gG4JZy9+NOzDEP0nbTlXAfFBB756oEkjMXN7iat+lz0oMjqfe/x6BXXGyRpnLchFlELshGAu2zJ/H+zFR8W5aeuvONm/a38SJLW8Rs0wS7EnDW5P5/4WZ5I2tTemM71gyU0ck9FaIW7lOG1t/V4wwBl4op9OoQV4O0bEOhxw5aXR3Hl2WQM6YzStSNlvcOZjfFT/H/WVTRzhk=~4535609~4274497; bm_sv=6BFEA3CD7C7F57FF65483FB87717B04D~YAAQZw8tF0ynBJmRAQAAh/i4nxgmy/Xp7QzIJ1s/19RelwG7Buvc+EE2ZcbUuX1XFYe7Q4MZ0TV1vvARG/vBvk+98tSVK7+vxQT9spzpvS36RvwJ+rmTI6OJObEEPznRbeXn7DscN380dJIfWcr1uKGOKNX8jm+FPJOzM6REr1cf7vnfPFfctaxdFKOkxA8BgIeifYZL7QDcMbLRhSu18iEu7dvhiEUfYQFtHXrI9Pr6THKNQumBk/M0a9Pl7iKSvDRsWYal~1; _dd_s=rum=0&expire=1724962662716',
        'ispublic': '0',
        'origin': 'https://servicos.energisa.com.br',
        'priority': 'u=1, i',
        'referer': 'https://servicos.energisa.com.br/faturas',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
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
        'ate': 'eyJhbGciOiJBMjU2S1ciLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwidHlwIjoiSldUIiwiY3R5IjoiSldUIn0.xdikPswHOBah81Kl_Se9x3MghTdy8IY-YE0g0hVbgx0XGNdYHFqpYGF5KGCxPN0SbW8Hb2KmFvRUZPDaWYvWWd1LP9JF_Kam.FoaVY74a9RZYjZoM_rHg7A.u6GX_8vGuLT-odZuHTtkfrEUifl_vQhJVInFHucFeHucZsTnY7fRKNs1gE2L8bpJTWAPs-dgGYeQKp6ieOa5qYddtCROTeaaupLaK0bCl8sdOpGrSPYoHVw5sGgu7oRaWpsVeLOE-iFGPBuNSJDuOGqCi5KLf4_3jN4004_h72OKoWf_9JJx-1AgKBn2qF6m-ouxTM0SZP4cHrHzMkFsXXkCAKuXWhlKpaEf6BlrOhDE86oFdJgP7b70JKFkA_OlMe2OCiccX5P6eF7Sg0iqQl_xufl3d2jGuiky8gAdR1dhTCZsv-dtnfiMBQJLhbSoQm_WFxtkPjASNi30uQwBk0c64ORF8ESlRbyd4wGvE3yDGPX1K6p5toqn-YCx3ayFUxHQT9zMLfILk4k6UbyB_1DYh6jHGS73AwXDi6AOdwkDCyqPUaVRUefLX9ihRCfeBc2INXv5_1gmehfgUSVHrofGdSEEfNfjPGxxzBwkJd55LYnwsXLumybcVXAztSQdo2hu5O75N2mqK6YhI5sPXVnA29-z0PRc8crTPeue8h2-mRGJwc2QTViBmYSRec7K0sg0VtJrZ2AWXDzPdTZT3HNYbo3ot7RN7GDMYIf7WlCf8TlRRQNG8m4u1nWtVMrcdGh4EZ5GsuewgkfKvuDu_c1z1a-Kf6kIy7DkhQnKwWVRqTImXperEQ3T6iwlVUlRHIG-urWCBe2W1DB_0iDHLTcR-4RAgeioMo2nD_fNFKSoImefzhEtK1CxfQEbcIYRUw3cuQcID_UzHKlyqHkqbKBwBstFIaNZ2c-ZX9jJBqGOr1J_jnqlklKu8yi338cjm9OGi5nl__tdQSicWYx2fO1tZ0vGqs4p8atHLPtqwqxneMGnr2WnhTj3ZLLwE5oh_0MEBKJ1FZwVEKsFH6X2FF9dhmOXmq1uQCs9uHjD4QziNuQ_Qv7v3CjBkGLQan8JaOn3EwHsttEoTeoMn8ZMC6AYgemomJxOnlsctSmzhYnHq9yuUvmHIo96KARabjeK.ipSg3_kxe0dPieBTjfWja7Va_sOFXqvzZnWvboA7AO8',
        'udk': 'EwBgLGDMCsCcBsAOOQ',
        'utk': 'eyJhbGciOiJBMjU2S1ciLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwidHlwIjoiSldUIiwiY3R5IjoiSldUIn0.wNgwz4bANDP47qaUCXBSG2e-r--uJQ1pc8AFTIVVLt4FZ4T9qEaYUo1AIFjAj80fKIktgV08O-Mu3Hy2UPiBAG_Ky9f348_v.qc4YPdfwC87Gk1Drtrhfug.aRg6hLVa19S5-yKmB9VPRZQip7LSnIjriG8iy9Gx6FfNSDhJUvLBBToNiYxyluJDltjoagZ7eBbJoWIDbGCm9kdaZDB0FTBAFYSXFHWz05R5jGsPBZknU49Pwcg3oMov_574XQhF4WczAy3j2DFb5Qy4L06p7WwS0cV7dVFzgX3Fg_lPZKyyfVWJW3ajqx9NkpHv7AdHRFK47JsHPsofNUfe3K2UxGZ4595YEhYGTzDLY8_SosIaNthsbXv_YRkq6FMS9V2ZMG19xFCdzNVBpytH1SuahV8yJLrjlzSzS0JegIzrMSovhYcI4mk2xdUqf-dDBPzvNFINx_TJGteYODHueCQnx6MIzA1077Jqj94lt3LRKp3nqo3wRgyc4CJ6Rgb7P3-R4u3gT6nTmH84i8ck3QyYheZSc8TzKUZXdSOuyamdegrQ-K4VpQ3m6KO6cygrPxCyaJBJplWPFT2lo6Fx9cHOoQwiwfr1gy3tQ-P0bdsabAp2FmCsTe1UMG5U7PlFKvdQ8kI6Hbm9927evW4ws6pyPsJuL9yVVkuvlS6DkpPM-2xJgYzNuZhuV-oS6IBybKfAFEqxgIY5wq5I5vLMcp1T1p4D1UKJXdLnKoSQlbnp9L3Vt4I_1TrLQzsVi4o_rZxjKJ0BloneHrz_TuBFFmlSE7cBst02Zemou6SZT5yjDuew2OUFhUsmG23WFOdHuj4xL8XmsAi2ws9Cx15BYanCB7lOTHh3TRWl2g2-LGADaWRF37Hrp4jtE08o2STIJU7yELnd8RNHPK__XJr0iFCqTJoPLaEtwmq0CeQ1wsHhACYucUh3BKstSB3rf-tXL4dh4xhqkx0SKMAZLBrb72PqImFwpD3RS38m1mi-gZ2gVK2zi40s5uZjxx3JdKDCRQ0iVvTwE5gxocnhfuAEjh2AwJ6ZaUpYIkIi_jwajAk2_AA7Rdp9UPVn0uKeL92ZuvOlYSX5-QORhgK904h8oUw8bDY5mnVBeAi8u3w3EfTb7Sg4W43fxBOzbwsbHQQGI-0zS4CnzCXHBAduBQz3uX9SXAel0pu_xY0Hn4aUjnsPAtQEOD4txuRhFxr8cMT9yYkc610_VKRsM89PS75DvfcVlDD_7k4sYw5uSas-vZrSHpjze-h5fHG4A1CICZUfPSCpFDegD89K29mqacgQyPtD05NFgWz6R8wCXBSW68zX519tuGyVyQTQ_gayubBuQlJkwGHjLA99ZUMelA.8xkzwIqAkw_vMXdZJPlDHll-5s3WqWrNLobN8x2CdZU',
        'refreshToken': 'a603dc95591dbbc3cfe14134e419e08bf8e6cb8b857550c62ee9f4ec61ab28ce006a928edbf74c2c1bc547ad41bee19a9816647fd328cec81b4a73277cc549ef',
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
    async_playwright()
    consultar_infos_cpf()
    code = '1631'
    acessar_code_seguranca(code)
    baixar_pdf()
