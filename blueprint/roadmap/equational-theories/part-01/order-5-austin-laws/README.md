# Order 5 Austin laws

[Finite implications and infinite models](../finite-implications-and-infinite-models/README.md) has useful background context for this chapter. As noted in [Finite implications and infinite models](../finite-implications-and-infinite-models/README.md): an *Austin law* is a law which admits infinite models, but no nontrivial finite models. Austin laws have order 5 or greater \[[Kisielewicz 1997](https://doi.org/10.1007/s000120050057)\]. In this chapter we report partial results of a classification of laws of order 5 on whether they do or do not allow non-trivial finite or infinite models, with a particular interest in finding Austin laws. This work is also discussed in [this Zulip thread](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/Some.20results.20from.20order.205/near/482118667) with results saved on [this git branch](https://github.com/vlad902/equational_theories/tree/order5).

There are 57,882 equations of order 5 (not including the 4,694 equations of order $\le 4$).

- 19,392 (33.5%) admit only trivial models.
- 38,360 (66.2%) have known satisfying finite models (and hence, also infinite models).
- 106 allow only trivial finite models. Of these, 10 are Austin laws, and it is unknown whether the remaining 96 admit infinite models.
- In 24 cases it is unknown whether they allow nontrivial finite models.

Of the equations with known satisfying finite models, a few had a minimum satisfying model size of order 17 (the largest minimum satisfying model size in order $\le 4$ is 7.) One equation was found with a satisfying model of order 26, but the smaller orders were not exhaustively searched so it cannot be established that the order is minimal.

### Equations with trivial finite models

106 equations were found that admitted only trivial finite models. Of these, Vampire's decision procedure finished without finding an implication to Equation 2 for 10 equations, allowing us to establish that they are inequivalent, e.g. they allow non-trivial infinite models. Hence, they must be Austin laws. The set of 10 Austin laws includes [E28770](https://teorth.github.io/equational_theories/implications/?28770) $({x = (((y \diamond y) \diamond y) \diamond x) \diamond (y \diamond z)})$, an Austin law established in \[[Kisielewicz 1997](https://doi.org/10.1007/s000120050057)\]. Note that Vampire's decision procedure also establishes that all 10 Austin laws are inequivalent to each other. These laws are listed in table1.

*(A table in the source is not reproduced here.)*

Of the 96 remaining equations, Vampire did not establish any implications between equations in this set. No effort was made to build infinite models for these equations. This set includes [E5093](https://teorth.github.io/equational_theories/implications/?5093) $({x = y \diamond (y \diamond (y \diamond (x \diamond (z \diamond y))))})$, another equation mentioned in \[[Kisielewicz 1997](https://doi.org/10.1007/s000120050057)\] as having only trivial finite models, and it being unknown whether it allows infinite models. These laws are listed in table2.

*(A table in the source is not reproduced here.)*

### Remaining unknown equations

There are 24 (12 modulo duality) remaining equations, for which we did not establish whether they do or do not admit nontrivial finite models. For one equation, Equation 17260 below, Vampire's decision procedure indicates that it admits nontrivial models, though it is unclear whether it admits nontrivial finite models. These laws are listed in table3.

*(A table in the source is not reproduced here.)*
