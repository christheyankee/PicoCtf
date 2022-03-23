import binascii
def pollard(n):
    a = 2
    i = 2
    while(True):
        a = pow(a,i,n)
        d = gcd((a-1), n)
        if (d > 1):
            return d
        i += 1
    
n = 11610761392735987177370291654492023317292242300550906204247440158468650972283185869299551637510455945339656522158686835946451505870917570819581316909050151220479920986903393027394294260965271853844521934955304245498928788993532458573653352840982168194750469188523525270346992030910759378374749021665972776252464601179257225938115001261580909824716805933735050392812291557145835112447403295596250092311373228026230572283175524535826085090441815708255828178418501943000096934688120380417168820601929542959128619035164412970917991511442695014429374223691506392746314441403384317885741608586053898413762350675914667486921
c = 287644306891588225546669610621118823548618836215255161320267747254008819894302436021794894424585865009175218062035232979896560954168995265571851594566320402483687233394152094697491688758635760936056292730905447997033830467567995730445749941907513135892806665374653365001435734295093673170817236699312179643045883947446061917688079299606142242075717189935237905737231459717912864418551074598209233574538416163973365175784361075830377571327873896235079684002071069146617864541339548127081847938153149939341964843668993331888382000647236229855123587618440519336254235852081229826982407112880859627377397549714900869614
g = 3
#p_factors = []

#p = Integer(pollard(n))
#q = n / p

# bound_1 = 33000
# bound_2 = 13200000
# for prime in [p, q]:
#     real_prime = 2
#     p_1 = primes(bound_1) 
#     l = list(p_1)
#     l.insert(0,1)
#     #undo outer shell (small primes)
#     for a in l:
#         if (float((prime - 1)) / (a)).is_integer():
#             real_prime = (prime - 1) / (a)
#             break
#     #undo inner shell (larger primes)
#     for q in primes(bound_2):
#         if real_prime % q == 0:
#             p_factors.append(q)
#     p_factors = []

p = 112702077491326624035437448311528244416633038267184436467539953783623022543629307291975209668348933325006075339780165463077524233511267597550006727923822554354936896793276829740193900248027487979522143806746878229772394053610558597354876381637035909859704552979985236170415302488615161107293296362528480525723
q = 103021715758784777065538393486053743054182192354548423680703519825749790456047554303092034581065984146706235372014968357870399173576106002085550048294579946475544854431226807856399757519538822807164181477730623920265727637084436385548675453295077723702870680050335729771811407346688861515254536686372633918827

g_x_p = Mod(c, p)
g_x_q = Mod(c, q)
for k in range(0,1):
    i = 38251710328773353864596243890570950490237 + 56351038745663312017718724155764122208316519133592218233769976891811511271814653645987604834174466662503037669890082731538762116755633798775003363961911277177468448396638414870096950124013743989761071903373439114886197026805279298677438190818517954929852276489992618085207651244307580553646648181264240262861 * k
    j = 38251710328773353864596243890570950490237 + 51510857879392388532769196743026871527091096177274211840351759912874895228023777151546017290532992073353117686007484178935199586788053001042775024147289973237772427215613403928199878759769411403582090738865311960132863818542218192774337726647538861851435340025167864885905703673344430757627268343186316959413 * k



    print(pow(3, i, p))
    print(g_x_p)

    x_prime = Integer(CRT([i, j], [p - 1, q - 1]))
    mult = lcm((p-1), (q-1))
    print("p:", p)
    print("q", q)
    prop_c = pow(3, int(x_prime), n)
    min = n
    print(pow(3, g_x_p, p))
    print(Mod(c, p))
    print(binascii.unhexlify(hex(x_prime)[2:]))