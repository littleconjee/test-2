import itertools as itls
cipher = '0wt1cx2t89x05pa3p5996p8t9cntuun8090nst2tan6x09v8ps1p0tts1rp0xncpcsap5tb6wp9x9ncr1a0x2p0xcvwxvwat2ta0patc09xc0wttp8a5iglh90wtn8xvxcpabxcxcvst6p80btc0nu0wttcvxctt8xcvxc90x010tnuw1cpc1cx2t89x050nnz0wtxcx0xp0x2t0n8tr81x06n90v8ps1p0t901stc09r188tc0a50wt8tp8tpqn10iifhhv8ps1p0t901stc09tc8naatsp00wt1cx2t89x05xcra1sxcvctp8a5jihhsnr0n8pa901stc09pcsn2t8ghhhbp90t8901stc096n90v8ps1p0t901stc09cn0nca5pr0x2ta56p80xrx6p0txc9rxtc0xuxr8t9tp8rwxc0wtx8n3csx9rx6axct9pcs96trxpa0xt9q10pa9n0pzt6p80xc2p8xn19prpstbxrt4rwpcvt9pcsrnb6t0x0xnc90wt5wp2tqtrnbtpcxb6n80pc06xaap8xcbpxc0pxcxcv0wt1cx2t89x059ancv08psx0xncnut4rt60xncpa9rwnap89wx6'

def encrypt(msg, key, code):
    before = code
    after = code[key:]+code[: key]
    table = ''.maketrans(before, after)
    return msg.translate(table)


def decrypt(cipher, key, code):
    before = code
    after = code[36-key:]+code[: 36-key]
    table = ''.maketrans(before, after)
    return cipher.translate(table)


code1 = 'abcdefghijklm'
code2 = 'nopqrstuvwxyz'
code3 = '01234'
code4 = '56789'

h1 = itls.permutations(code1)
h2 = itls.permutations(code2)
h3 = itls.permutations(code3)
h4 = itls.permutations(code4)

for key in range(1, 36):
    for i in h1:
        h2 = itls.permutations(code2)
        for j in h2:
            h3 = itls.permutations(code3)
            for k in h3:
                h4 = itls.permutations(code4)
                for p in h4:
                    code = ''.join(i+j+k+p)
                    msgtest = decrypt(cipher, key, code)
                    print(msgtest)


from collections import Counter
a=Counter(cipher)
a.items()
print(a.most_common(29))


table = ''.maketrans('wlcpc1cx2t89x05', 'hunanuniversity')
print(cipher.translate(table))

#密文‘0wt1cx2t89x05pa3p5996p8t9cntuun8090nst2tan6x09v8ps1p0tts1rp0xncpcsap5tb6wp9x9ncr1a0x2p0xcvwxvwat2ta0patc09xc0wttp8a5iglh90wtn8xvxcpabxcxcvst6p80btc0nu0wttcvxctt8xcvxc90x010tnuw1cpc1cx2t89x050nnz0wtxcx0xp0x2t0n8tr81x06n90v8ps1p0t901stc09r188tc0a50wt8tp8tpqn10iifhhv8ps1p0t901stc09tc8naatsp00wt1cx2t89x05xcra1sxcvctp8a5jihhsnr0n8pa901stc09pcsn2t8ghhhbp90t8901stc096n90v8ps1p0t901stc09cn0nca5pr0x2ta56p80xrx6p0txc9rxtc0xuxr8t9tp8rwxc0wtx8n3csx9rx6axct9pcs96trxpa0xt9q10pa9n0pzt6p80xc2p8xn19prpstbxrt4rwpcvt9pcsrnb6t0x0xnc90wt5wp2tqtrnbtpcxb6n80pc06xaap8xcbpxc0pxcxcv0wt1cx2t89x059ancv08psx0xncnut4rt60xncpa9rwnap89wx6’
#能表示的明文‘the university aa3ayss6 are snneuunrtstnsevean6 its vrasuateesuratinnansaayeb6hasisnnruativatinvhivhaeveataaentsintheearayiguhsthenrivinaabininvse6artbentnutheenvineerinvinstitutenu hunan university tnnztheinitiativetnrerruit6nstvrasuatestusentsrurrentaythere are aqnutiifhhvrasuatestusentsenrnaaesat the university inrausinvnearayjihhsnrtnraastusentsansnverghhhbasterstusents6nstvrasuatestusentsnntnnayartiveay6artiri6ateinsrientiuirresearrhintheirn3nsisri6ainesanss6eriaatiesqutaasntaze6artinvarinusarasebire4rhanvesansrnb6etitinns they have qernbeanib6nrtant6iaaarinbaintaininv the university sannvtrasitinnnue4re6tinnaasrhnaarshi6’
