#!/usr/bin/python3

import numpy as np

out = np.array([-0.04613495 -0.04606819 -0.04667282 -0.0466671  -0.04641724 -0.04659462
 -0.04750443 -0.04688835 -0.0471859  -0.04748726 -0.0472374  -0.04729271
 -0.0476532  -0.04776764 -0.04794502 -0.04781723 -0.048666   -0.04908752
 -0.04847145 -0.04901505 -0.04906845 -0.04869652 -0.04862976 -0.04893112
 -0.04892349 -0.04903984 -0.05001068 -0.04927254 -0.04957008 -0.04968452
 -0.04968071 -0.0500412  -0.0497303  -0.05014992 -0.0503273  -0.0498333
 -0.0507431  -0.04988098 -0.05072784 -0.05078506 -0.05096245 -0.05034637
 -0.05137444 -0.0516758  -0.05093575 -0.05086899 -0.05153275 -0.0514679
 -0.051157   -0.05187988 -0.05163002 -0.0514431  -0.05198669 -0.0511837
 -0.05172729 -0.05135536 -0.05256844 -0.05152512 -0.05231285 -0.05193901
 -0.05272865 -0.05235672 -0.05265236 -0.05246544 -0.0522747  -0.05275536
 -0.05311584 -0.05268288 -0.05182076 -0.05291367 -0.05235672 -0.05332756
 -0.05240631 -0.05276489 -0.05306435 -0.05256844 -0.05292892 -0.05335236
 -0.05340576 -0.05291176 -0.05308533 -0.05265236 -0.05313492 -0.05294418
 -0.05348778 -0.05262566 -0.05268288 -0.05395889 -0.05273056 -0.05339432
 -0.0535717  -0.05289268 -0.05343628 -0.0530014  -0.05318069 -0.05304909
 -0.05340958 -0.05273247 -0.05235863 -0.05210876 -0.05283546 -0.05331612
 -0.05331039 -0.05373001 -0.05299187 -0.05231476 -0.05249214 -0.05248642
 -0.05241776 -0.05296135 -0.05197906 -0.05270195 -0.05312347 -0.05293655
 -0.05305099 -0.05298233 -0.05242729 -0.05236053 -0.0519886  -0.05204201
 -0.05234146 -0.05245781 -0.05202293 -0.05311394 -0.05304909 -0.05218697
 -0.05297279 -0.05174828 -0.05155754 -0.05179596 -0.05185127 -0.05184364
 -0.05195999 -0.05238152 -0.05182457 -0.05230522 -0.05205727 -0.05211067
 -0.05198288 -0.05124474 -0.05111504 -0.05141449 -0.0514698  -0.05207443
 -0.05194473 -0.05108452 -0.0522995  -0.05180359 -0.05118752 -0.051548
 -0.05074692 -0.0507412  -0.05116272 -0.05097389 -0.05133438 -0.05150986
 -0.05125999 -0.05119133 -0.05088043 -0.05081367 -0.05111313 -0.0498848
 -0.05073357 -0.05018044 -0.05029678 -0.04986191 -0.05009842 -0.05015373
 -0.04990578 -0.04941177 -0.0500145  -0.05000687 -0.0495739  -0.04956818
 -0.05017281 -0.04925346 -0.0491848  -0.04942322 -0.04978371 -0.04898453
 -0.04867363 -0.04860497 -0.04890442 -0.04889679 -0.0489521  -0.0486412
 -0.0490036  -0.04832649 -0.04752731 -0.0478878  -0.04745483 -0.04763222
 -0.04732132 -0.04804802 -0.04749298 -0.04730415 -0.04803085 -0.0471096
 -0.04704094 -0.04660797 -0.04727364 -0.04665756 -0.04659081 -0.04652405
 -0.04609108 -0.04547691 -0.04602242 -0.04656601 -0.04521751 -0.04551506
 -0.04465485 -0.04507828 -0.04501152 -0.04512787 -0.04444885 -0.04413986
 -0.0449276  -0.04418945 -0.0441246  -0.04393578 -0.04374886 -0.04362297
 -0.04349327 -0.04318237 -0.04299355 -0.04390335 -0.04341316 -0.04279518
 -0.04279137 -0.04302788 -0.04210854 -0.04137039 -0.04179192 -0.04117775
 -0.04178429 -0.04171753 -0.04146957 -0.04128075 -0.04090881 -0.04084396
 -0.0405941  -0.04059029 -0.04027939 -0.03978539 -0.04026985 -0.03977585
 -0.03885651 -0.03878975 -0.03964043 -0.03926849 -0.0387764  -0.03877068
 -0.03833961 -0.03784561 -0.03747749 -0.03796005 -0.03832245 -0.03734016
 -0.03739548 -0.03739357 -0.03763199 -0.03713799 -0.03646469 -0.03639793
 -0.0358448  -0.03577995 -0.03534698 -0.03558731 -0.03515625 -0.03533745
 -0.03471947 -0.03477669 -0.03501892 -0.0346489  -0.03409195 -0.0336628
 -0.03347588 -0.03341103 -0.03328514 -0.03309822 -0.03254318 -0.0324173
 -0.03259659 -0.03204346 -0.03149033 -0.03106117 -0.03099442 -0.0308075
 -0.0304985  -0.03074074 -0.03104019 -0.0305481  -0.03017998 -0.02956581
 -0.03005219 -0.02974319 -0.0292511  -0.02851486 -0.0291214  -0.02807999
 -0.02844238 -0.02850151 -0.02788734 -0.02824974 -0.02714729 -0.02696037
 -0.02744865 -0.02665138 -0.02609825 -0.02554512 -0.02560234 -0.02541542
 -0.02541542 -0.02528954 -0.0255909  -0.02442932 -0.02442551 -0.02308083
 -0.02289391 -0.02368546 -0.02325439 -0.02313042 -0.02276039 -0.02312469
 -0.02220535 -0.02250862 -0.02250671 -0.02189445 -0.02207565 -0.02085114
 -0.02152061 -0.02133369 -0.02084351 -0.02090263 -0.02053261 -0.02114105
 -0.02077293 -0.02009773 -0.01905823 -0.01862907 -0.01887321 -0.01893044
 -0.01795006 -0.01807213 -0.0185585  -0.01861763 -0.0177002  -0.01769638
 -0.01696205 -0.01665497 -0.01701927 -0.01665115 -0.01573372 -0.01567078
 -0.01573181 -0.01530266 -0.01481056 -0.0141983  -0.01468658 -0.01425552
 -0.01413345 -0.01394844 -0.01284981 -0.01351929 -0.01302719 -0.0121727
 -0.0123539  -0.01229095 -0.0114975  -0.01204491 -0.01088524 -0.01143074
 -0.01021194 -0.01106453 -0.00953484 -0.01008606 -0.01038933 -0.00977707
 -0.00916672 -0.00916481 -0.00837135 -0.00904083 -0.00824738 -0.00757408])

a = np.mean(np.square(out))
print('mean-square: %5.2f' % a)

b = np.sqrt(a)
print('rms: %5.2f' % b)

c = np.log10(b)
print('log10: %5.2f' % c)

d = 20*c
print('db20: %5.2f' % d)