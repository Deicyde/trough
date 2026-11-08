---
declaration: theorem
origin: cited
lean: TauCeti.poincarePolynomial_map
statement: formalized
proof: formalized
---

# The Poincaré polynomial is invariant under transporting the Coxeter system along a group isomorphism, since the length function is (`TauCeti.length_map`)

The hypothesis `[Finite H]`
follows from `[Finite W]`, but is needed to state the left-hand side.

```lean
TauCeti.poincarePolynomial_map.{u_1, u_2, u_4} {B : Type u_1} {W : Type u_2} [Group W]
  {M : CoxeterMatrix B} (cs : CoxeterSystem M W) {H : Type u_4} [Group H] [Finite W] [Finite H]
  (e : W ≃* H) : TauCeti.poincarePolynomial (cs.map e) = TauCeti.poincarePolynomial cs
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.poincarePolynomial_map`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Coxeter/Poincare.html#TauCeti.poincarePolynomial_map).

## Sources

- [Tau Ceti documentation: `TauCeti.poincarePolynomial_map`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Coxeter/Poincare.html#TauCeti.poincarePolynomial_map)
- [Source of `TauCeti.poincarePolynomial_map` in TauCeti/GroupTheory/Coxeter/Poincare.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Coxeter/Poincare.lean#L217)
