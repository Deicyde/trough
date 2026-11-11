---
declaration: theorem
origin: cited
lean: CoxeterSystem.exists_wordProd_alternatingWord_mul_of_isLeftDescent_pair
statement: formalized
proof: formalized
---

# Tits' lemma

If `i ≠ i'` are both left descents of `w`, then `w` splits as a rank-two
parabolic factor times a remainder, the lengths adding, and the parabolic factor is spelled by
*both* alternating words of length `orderOf (s i * s i')`.

Classically the exponent is the Coxeter-matrix entry `M i i'`; the order of `s i * s i'` divides it
(`CoxeterSystem.simple_mul_simple_pow`), which gives the bound
`CoxeterSystem.length_le_of_isLeftDescent_pair`, and the two agree by Tits' theorem on the
geometric representation — see the module docstring.

```lean
CoxeterSystem.exists_wordProd_alternatingWord_mul_of_isLeftDescent_pair.{u_1, u_2} {B : Type u_1}
  {W : Type u_2} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W) {i i' : B} (hne : i ≠ i')
  {w : W} (hd : cs.IsLeftDescent w i) (hd' : cs.IsLeftDescent w i') :
  ∃ v,
    0 < orderOf (cs.simple i * cs.simple i') ∧
      w =
          cs.wordProd (CoxeterSystem.alternatingWord i i' (orderOf (cs.simple i * cs.simple i'))) *
            v ∧
        w =
            cs.wordProd
                (CoxeterSystem.alternatingWord i' i (orderOf (cs.simple i * cs.simple i'))) *
              v ∧
          cs.length w = orderOf (cs.simple i * cs.simple i') + cs.length v
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CoxeterSystem.exists_wordProd_alternatingWord_mul_of_isLeftDescent_pair`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Coxeter/Dihedral.html#CoxeterSystem.exists_wordProd_alternatingWord_mul_of_isLeftDescent_pair).

## Sources

- [Tau Ceti documentation: `CoxeterSystem.exists_wordProd_alternatingWord_mul_of_isLeftDescent_pair`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Coxeter/Dihedral.html#CoxeterSystem.exists_wordProd_alternatingWord_mul_of_isLeftDescent_pair)
- [Source of `CoxeterSystem.exists_wordProd_alternatingWord_mul_of_isLeftDescent_pair` in TauCeti/GroupTheory/Coxeter/Dihedral.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Coxeter/Dihedral.lean#L319)
