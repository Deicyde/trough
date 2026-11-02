# Order 5 Austin laws

[Finite implications and infinite models](../finite-implications-and-infinite-models/README.md) has useful background context for this chapter. As noted in [Finite implications and infinite models](../finite-implications-and-infinite-models/README.md): an *Austin law* is a law which admits infinite models, but no nontrivial finite models. Austin laws have order 5 or greater ([Kisielewicz 1997](https://doi.org/10.1007/s000120050057)). In this chapter we report partial results of a classification of laws of order 5 on whether they do or do not allow non-trivial finite or infinite models, with a particular interest in finding Austin laws. This work is also discussed in [this Zulip thread](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/Some.20results.20from.20order.205/near/482118667) with results saved on [this git branch](https://github.com/vlad902/equational_theories/tree/order5).

There are 57,882 equations of order 5 (not including the 4,694 equations of order $\le 4$).

- 19,392 (33.5%) admit only trivial models.
- 38,360 (66.2%) have known satisfying finite models (and hence, also infinite models).
- 106 allow only trivial finite models. Of these, 10 are Austin laws, and it is unknown whether the remaining 96 admit infinite models.
- In 24 cases it is unknown whether they allow nontrivial finite models.

Of the equations with known satisfying finite models, a few had a minimum satisfying model size of order 17 (the largest minimum satisfying model size in order $\le 4$ is 7.) One equation was found with a satisfying model of order 26, but the smaller orders were not exhaustively searched so it cannot be established that the order is minimal.

## Equations with trivial finite models

106 equations were found that admitted only trivial finite models. Of these, Vampire's decision procedure finished without finding an implication to Equation 2 for 10 equations, allowing us to establish that they are inequivalent, e.g. they allow non-trivial infinite models. Hence, they must be Austin laws. The set of 10 Austin laws includes [E28770](https://teorth.github.io/equational_theories/implications/?28770) $({x = (((y \diamond y) \diamond y) \diamond x) \diamond (y \diamond z)})$, an Austin law established in ([Kisielewicz 1997](https://doi.org/10.1007/s000120050057)). Note that Vampire's decision procedure also establishes that all 10 Austin laws are inequivalent to each other. These laws are listed in Table 1.

| $x = y \diamond (x \diamond (x \diamond (y \diamond (z \diamond z))))$ (4916) | $x = ((((y \diamond y) \diamond z) \diamond x) \diamond x) \diamond z$ (41082) |
| --- | --- |
| $x = y \diamond (((x \diamond (z \diamond z)) \diamond y) \diamond y)$ (15535) | $x = (y \diamond (y \diamond ((z \diamond z) \diamond x))) \diamond y$ (30591) |
| $x = (y \diamond z) \diamond (x \diamond (z \diamond (z \diamond z)))$ (17522) | $x = (((y \diamond y) \diamond y) \diamond x) \diamond (y \diamond z)$ (28770) |
| $x = (y \diamond y) \diamond ((z \diamond (x \diamond x)) \diamond z)$ (20034) | $x = (y \diamond ((x \diamond x) \diamond y)) \diamond (z \diamond z)$ (25964) |
| $x = (y \diamond (x \diamond x)) \diamond ((y \diamond z) \diamond y)$ (22455) | $x = (y \diamond (z \diamond y)) \diamond ((x \diamond x) \diamond y)$ (22818) |

**Table 1.** Austin laws

Of the 96 remaining equations, Vampire did not establish any implications between equations in this set. No effort was made to build infinite models for these equations. This set includes [E5093](https://teorth.github.io/equational_theories/implications/?5093) $({x = y \diamond (y \diamond (y \diamond (x \diamond (z \diamond y))))})$, another equation mentioned in ([Kisielewicz 1997](https://doi.org/10.1007/s000120050057)) as having only trivial finite models, and it being unknown whether it allows infinite models. These laws are listed in Table 2.

| $x = y \diamond (x \diamond (y \diamond (y \diamond (z \diamond y))))$ (4952) | $x = ((((y \diamond z) \diamond y) \diamond y) \diamond x) \diamond y$ (41252) |
| --- | --- |
| $x = y \diamond (x \diamond (y \diamond (z \diamond (x \diamond z))))$ (4957) | $x = ((((y \diamond x) \diamond y) \diamond z) \diamond x) \diamond z$ (40914) |
| $x = y \diamond (x \diamond (z \diamond (z \diamond (y \diamond z))))$ (5012) | $x = ((((y \diamond z) \diamond y) \diamond y) \diamond x) \diamond z$ (41253) |
| $x = y \diamond (y \diamond (x \diamond (y \diamond (z \diamond y))))$ (5066) | $x = ((((y \diamond z) \diamond y) \diamond x) \diamond y) \diamond y$ (41239) |
| $x = y \diamond (y \diamond (y \diamond (x \diamond (z \diamond y))))$ (5093) | $x = ((((y \diamond z) \diamond x) \diamond y) \diamond y) \diamond y$ (41179) |
| $x = y \diamond (y \diamond (y \diamond (z \diamond (x \diamond y))))$ (5107) | $x = ((((y \diamond x) \diamond z) \diamond y) \diamond y) \diamond y$ (40951) |
| $x = y \diamond (y \diamond (z \diamond (y \diamond (x \diamond y))))$ (5141) | $x = ((((y \diamond x) \diamond y) \diamond z) \diamond y) \diamond y$ (40917) |
| $x = y \diamond (z \diamond (y \diamond (y \diamond (x \diamond y))))$ (5295) | $x = ((((y \diamond x) \diamond y) \diamond y) \diamond z) \diamond y$ (40909) |
| $x = y \diamond (x \diamond (y \diamond ((z \diamond x) \diamond y)))$ (5833) | $x = (((y \diamond (x \diamond z)) \diamond y) \diamond x) \diamond y$ (40070) |
| $x = y \diamond (x \diamond (y \diamond ((z \diamond x) \diamond z)))$ (5834) | $x = (((y \diamond (x \diamond y)) \diamond z) \diamond x) \diamond z$ (40037) |
| $x = y \diamond (x \diamond (y \diamond ((z \diamond y) \diamond y)))$ (5837) | $x = (((y \diamond (y \diamond z)) \diamond y) \diamond x) \diamond y$ (40221) |
| $x = y \diamond (y \diamond (x \diamond ((z \diamond x) \diamond y)))$ (5947) | $x = (((y \diamond (x \diamond z)) \diamond x) \diamond y) \diamond y$ (40057) |
| $x = y \diamond (y \diamond (x \diamond ((z \diamond y) \diamond y)))$ (5951) | $x = (((y \diamond (y \diamond z)) \diamond x) \diamond y) \diamond y$ (40208) |
| $x = y \diamond (y \diamond ((x \diamond y) \diamond (z \diamond y)))$ (6820) | $x = (((y \diamond z) \diamond (y \diamond x)) \diamond y) \diamond y$ (39485) |
| $x = y \diamond (y \diamond ((z \diamond x) \diamond (x \diamond y)))$ (6878) | $x = (((y \diamond x) \diamond (x \diamond z)) \diamond y) \diamond y$ (39126) |
| $x = y \diamond (y \diamond ((z \diamond y) \diamond (x \diamond y)))$ (6895) | $x = (((y \diamond x) \diamond (y \diamond z)) \diamond y) \diamond y$ (39163) |
| $x = y \diamond (y \diamond ((z \diamond z) \diamond (x \diamond y)))$ (6912) | $x = (((y \diamond x) \diamond (z \diamond z)) \diamond y) \diamond y$ (39214) |
| $x = y \diamond (x \diamond ((y \diamond (z \diamond x)) \diamond y))$ (7587) | $x = ((y \diamond ((x \diamond z) \diamond y)) \diamond x) \diamond y$ (38316) |
| $x = y \diamond (y \diamond ((x \diamond (z \diamond x)) \diamond y))$ (7701) | $x = ((y \diamond ((x \diamond z) \diamond x)) \diamond y) \diamond y$ (38303) |
| $x = y \diamond (y \diamond ((z \diamond (x \diamond x)) \diamond y))$ (7755) | $x = ((y \diamond ((x \diamond x) \diamond z)) \diamond y) \diamond y$ (38249) |
| $x = y \diamond (y \diamond ((z \diamond (x \diamond z)) \diamond y))$ (7763) | $x = ((y \diamond ((z \diamond x) \diamond z)) \diamond y) \diamond y$ (38565) |
| $x = y \diamond (x \diamond (((z \diamond x) \diamond y) \diamond y))$ (8485) | $x = ((y \diamond (y \diamond (x \diamond z))) \diamond x) \diamond y$ (37519) |
| $x = y \diamond ((x \diamond y) \diamond (y \diamond (z \diamond y)))$ (9337) | $x = (((y \diamond z) \diamond y) \diamond (y \diamond x)) \diamond y$ (36867) |
| $x = y \diamond ((x \diamond y) \diamond (z \diamond (y \diamond y)))$ (9345) | $x = (((y \diamond y) \diamond z) \diamond (y \diamond x)) \diamond y$ (36713) |
| $x = y \diamond ((x \diamond z) \diamond (y \diamond (z \diamond z)))$ (9384) | $x = (((y \diamond y) \diamond z) \diamond (y \diamond x)) \diamond z$ (36714) |
| $x = y \diamond ((z \diamond x) \diamond (y \diamond (x \diamond y)))$ (9603) | $x = (((y \diamond x) \diamond y) \diamond (x \diamond z)) \diamond y$ (36514) |
| $x = y \diamond ((z \diamond y) \diamond (x \diamond (x \diamond y)))$ (9663) | $x = (((y \diamond x) \diamond x) \diamond (y \diamond z)) \diamond y$ (36487) |
| $x = y \diamond ((z \diamond y) \diamond (x \diamond (y \diamond y)))$ (9667) | $x = (((y \diamond y) \diamond x) \diamond (y \diamond z)) \diamond y$ (36638) |
| $x = y \diamond ((z \diamond y) \diamond (y \diamond (x \diamond y)))$ (9680) | $x = (((y \diamond x) \diamond y) \diamond (y \diamond z)) \diamond y$ (36524) |
| $x = y \diamond ((x \diamond y) \diamond ((z \diamond x) \diamond y))$ (10218) | $x = ((y \diamond (x \diamond z)) \diamond (y \diamond x)) \diamond y$ (35685) |
| $x = y \diamond ((x \diamond y) \diamond ((z \diamond y) \diamond y))$ (10222) | $x = ((y \diamond (y \diamond z)) \diamond (y \diamond x)) \diamond y$ (35836) |
| $x = y \diamond ((x \diamond (y \diamond x)) \diamond (z \diamond y))$ (11081) | $x = ((y \diamond z) \diamond ((x \diamond y) \diamond x)) \diamond y$ (35036) |
| $x = y \diamond ((x \diamond (y \diamond x)) \diamond (z \diamond z))$ (11082) | $x = ((y \diamond y) \diamond ((x \diamond z) \diamond x)) \diamond z$ (34889) |
| $x = y \diamond ((x \diamond (z \diamond x)) \diamond (y \diamond y))$ (11116) | $x = ((y \diamond y) \diamond ((x \diamond z) \diamond x)) \diamond y$ (34888) |
| $x = y \diamond ((y \diamond (x \diamond y)) \diamond (z \diamond y))$ (11205) | $x = ((y \diamond z) \diamond ((y \diamond x) \diamond y)) \diamond y$ (35100) |
| $x = y \diamond ((y \diamond (z \diamond y)) \diamond (x \diamond y))$ (11280) | $x = ((y \diamond x) \diamond ((y \diamond z) \diamond y)) \diamond y$ (34778) |
| $x = y \diamond (((y \diamond x) \diamond x) \diamond (z \diamond z))$ (12073) | $x = ((y \diamond y) \diamond (x \diamond (x \diamond z))) \diamond z$ (33998) |
| $x = y \diamond (((y \diamond x) \diamond z) \diamond (x \diamond z))$ (12087) | $x = ((y \diamond x) \diamond (y \diamond (x \diamond z))) \diamond z$ (33884) |
| $x = y \diamond (((z \diamond x) \diamond y) \diamond (x \diamond y))$ (12234) | $x = ((y \diamond x) \diamond (y \diamond (x \diamond z))) \diamond y$ (33883) |
| $x = y \diamond ((x \diamond (y \diamond (z \diamond z))) \diamond y)$ (12857) | $x = (y \diamond (((z \diamond z) \diamond y) \diamond x)) \diamond y$ (33436) |
| $x = y \diamond ((x \diamond (z \diamond (y \diamond x))) \diamond y)$ (12883) | $x = (y \diamond (((x \diamond y) \diamond z) \diamond x)) \diamond y$ (33020) |
| $x = y \diamond ((x \diamond ((z \diamond y) \diamond y)) \diamond y)$ (13764) | $x = (y \diamond ((y \diamond (y \diamond z)) \diamond x)) \diamond y$ (32294) |
| $x = y \diamond ((y \diamond ((x \diamond z) \diamond z)) \diamond z)$ (13849) | $x = (y \diamond ((y \diamond (y \diamond x)) \diamond z)) \diamond z$ (32281) |
| $x = y \diamond ((z \diamond ((x \diamond y) \diamond y)) \diamond y)$ (13992) | $x = (y \diamond ((y \diamond (y \diamond x)) \diamond z)) \diamond y$ (32280) |
| $x = (y \diamond x) \diamond (z \diamond ((x \diamond z) \diamond z))$ (18137) | $x = ((y \diamond (y \diamond x)) \diamond y) \diamond (x \diamond z)$ (27863) |
| $x = (y \diamond y) \diamond (x \diamond ((x \diamond z) \diamond z))$ (18212) | $x = ((y \diamond (y \diamond x)) \diamond x) \diamond (z \diamond z)$ (27859) |
| $x = (y \diamond y) \diamond ((x \diamond (x \diamond z)) \diamond z)$ (19966) | $x = (y \diamond ((y \diamond x) \diamond x)) \diamond (z \diamond z)$ (26105) |
| $x = (y \diamond (y \diamond x)) \diamond ((z \diamond z) \diamond z)$ (22619) | $x = (y \diamond (y \diamond y)) \diamond ((x \diamond z) \diamond z)$ (22634) |

**Table 2.** Trivial finite models, unknown infinite models

## Remaining unknown equations

There are 24 (12 modulo duality) remaining equations, for which we did not establish whether they do or do not admit nontrivial finite models. For one equation, Equation 17260 below, Vampire's decision procedure indicates that it admits nontrivial models, though it is unclear whether it admits nontrivial finite models. These laws are listed in Table 3.

| $x = y \diamond (((z \diamond y) \diamond x) \diamond (x \diamond y))$ (12294) | $x = ((y \diamond x) \diamond (x \diamond (y \diamond z))) \diamond y$ (33856) |
| --- | --- |
| $x = y \diamond ((z \diamond (x \diamond (x \diamond z))) \diamond y)$ (13102) | $x = (y \diamond (((z \diamond x) \diamond x) \diamond z)) \diamond y$ (33273) |
| $x = (y \diamond x) \diamond (z \diamond (x \diamond (z \diamond z)))$ (17260) | $x = (((y \diamond y) \diamond x) \diamond y) \diamond (x \diamond z)$ (28740) |
| $x = (y \diamond x) \diamond (z \diamond (z \diamond (x \diamond z)))$ (17286) | $x = (((y \diamond x) \diamond y) \diamond y) \diamond (x \diamond z)$ (28626) |
| $x = (y \diamond y) \diamond (((z \diamond x) \diamond x) \diamond z)$ (20911) | $x = (y \diamond (x \diamond (x \diamond y))) \diamond (z \diamond z)$ (25087) |
| $x = (y \diamond (y \diamond x)) \diamond (x \diamond (x \diamond z))$ (21714) | $x = ((y \diamond x) \diamond x) \diamond ((x \diamond z) \diamond z)$ (24200) |
| $x = (y \diamond (z \diamond x)) \diamond (x \diamond (x \diamond y))$ (21864) | $x = ((y \diamond x) \diamond x) \diamond ((x \diamond z) \diamond y)$ (24199) |
| $x = (y \diamond (z \diamond x)) \diamond (x \diamond (x \diamond z))$ (21865) | $x = ((y \diamond x) \diamond x) \diamond ((x \diamond y) \diamond z)$ (24197) |
| $x = (y \diamond (z \diamond x)) \diamond (x \diamond (x \diamond w))$ (21866) | $x = ((y \diamond x) \diamond x) \diamond ((x \diamond z) \diamond w)$ (24201) |
| $x = (y \diamond (x \diamond x)) \diamond ((x \diamond z) \diamond z)$ (22446) | $x = (y \diamond (y \diamond x)) \diamond ((x \diamond x) \diamond z)$ (22591) |
| $x = ((y \diamond x) \diamond x) \diamond (z \diamond (x \diamond z))$ (23337) | $x = ((y \diamond x) \diamond y) \diamond (x \diamond (x \diamond z))$ (23354) |
| $x = ((y \diamond x) \diamond y) \diamond (x \diamond (y \diamond z))$ (23357) | $x = ((y \diamond z) \diamond x) \diamond (z \diamond (x \diamond z))$ (23653) |

**Table 3.** Unknown whether they admit finite models
