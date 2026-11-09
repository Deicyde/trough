# 2. Frey package

> **2. Frey package.** A Frey package (`Definitions/Def_FLTPrelim_FreyPackage.lean`, adapted from the Imperial College
> London FLT project) is a solution a^p + b^p = c^p in nonzero integers, p ≥ 5 prime, normalised to gcd(a,b) = 1,
> a ≡ 3 (mod 4), 2 | b, with the Frey curve E\_P : y² + xy = x³ + ((b^p − 1 − a^p)/4)x² − (a^p b^p/16)x, an integral
> model of y² = x(x − a^p)(x + b^p). `FreyPackage.of_counterexample` builds one from any counterexample in nonzero integers with prime exponent
> p ≥ 5 (citing only Mathlib); `FreyPackage.no_frey_package (P : FreyPackage) : False` is assembled from exactly the four theorems of steps
> 3 to 6: irreducible and modular gives, after level lowering, a nonzero weight-2 cusp form on Γ₀(2), and there is
> none.

*Quoted from the route of the proof in [PROOF-PATH.md](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/PROOF-PATH.md) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0.*

The landmarks the repository's web pages place in this step, in the order this step names them:

- [FreyPackage.of_counterexample](freypackage-of-counterexample.md)
- [FreyPackage.no_frey_package](freypackage-no-frey-package.md)
