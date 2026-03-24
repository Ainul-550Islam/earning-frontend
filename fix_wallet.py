content = open('src/pages/Wallet.jsx', encoding='utf-8').read()

content = content.replace(
    'useState(MOCK_SUMMARY)',
    'useState({})'
).replace(
    'useState(MOCK_WALLETS)',
    'useState([])'
).replace(
    'useState(MOCK_TRANSACTIONS)',
    'useState([])'
).replace(
    'useState(MOCK_WITHDRAWALS)',
    'useState([])'
).replace(
    'useState(MOCK_METHODS)',
    'useState([])'
).replace(
    'wList.length ? wList : MOCK_WALLETS',
    'wList'
).replace(
    'txList.length ? txList : MOCK_TRANSACTIONS',
    'txList'
).replace(
    'wdList.length ? wdList : MOCK_WITHDRAWALS',
    'wdList'
).replace(
    'mList.length ? mList : MOCK_METHODS',
    'mList'
)

open('src/pages/Wallet.jsx', 'w', encoding='utf-8').write(content)
print('SUCCESS')
