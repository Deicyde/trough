---
declaration: def
origin: cited
lean: HeckeRing.GL2.Newform.atkinLehnerPseudoEigenvalue
statement: formalized
---

# The Atkin–Li pseudo-eigenvalue

**The Atkin–Li pseudo-eigenvalue** `λ_Q(f)` of a newform `f` at an exact divisor `Q` of the
level: the scalar with `𝒲_Q f = λ_Q(f) • g`, where `𝒲_Q` is the slash by the Atkin–Li matrix
`atkinLiMatrix N Q` normalized by `(√Q) ^ (2 - k)` and `g = f.atkinLehnerTransform h` is the
transported newform. Since `g` has first Fourier coefficient `1`, it is the first Fourier
coefficient of `𝒲_Q f`.

```lean
HeckeRing.GL2.Newform.atkinLehnerPseudoEigenvalue {N Q : ℕ} [NeZero N] {k : ℤ}
  (f : HeckeRing.GL2.Newform N k) (h : TauCeti.Nat.IsExactDivisor Q N) : ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Shimura's commutativity criterion (Proposition 3.8 of \[Shimura\]\[shimura1971\])](../../part-02/hecke-ring/shimuras-commutativity-criterion-proposition-3-8.md)
- [Shimura's decomposition of a double coset into right cosets](../../part-02/hecke-ring/shimuras-decomposition-of-a-double-coset-into-ri.md)

## Lean

Formalized in Tau Ceti as [`HeckeRing.GL2.Newform.atkinLehnerPseudoEigenvalue`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/AtkinLehner/PseudoEigenvalue.html#HeckeRing.GL2.Newform.atkinLehnerPseudoEigenvalue).

## Sources

- [Tau Ceti documentation: `HeckeRing.GL2.Newform.atkinLehnerPseudoEigenvalue`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/AtkinLehner/PseudoEigenvalue.html#HeckeRing.GL2.Newform.atkinLehnerPseudoEigenvalue)
- [Source of `HeckeRing.GL2.Newform.atkinLehnerPseudoEigenvalue` in TauCeti/NumberTheory/ModularForms/AtkinLehner/PseudoEigenvalue.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/AtkinLehner/PseudoEigenvalue.lean#L89)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ModularForms/STATUS.md)
