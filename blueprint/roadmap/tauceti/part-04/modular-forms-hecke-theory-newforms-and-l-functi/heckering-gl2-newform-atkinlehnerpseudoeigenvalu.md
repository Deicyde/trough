---
declaration: def
origin: cited
lean: HeckeRing.GL2.Newform.atkinLehnerPseudoEigenvalue
statement: formalized
---

# HeckeRing.GL2.Newform.atkinLehnerPseudoEigenvalue

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

## Lean

Formalized in Tau Ceti as [`HeckeRing.GL2.Newform.atkinLehnerPseudoEigenvalue`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/AtkinLehner/PseudoEigenvalue.html#HeckeRing.GL2.Newform.atkinLehnerPseudoEigenvalue).

## Sources

- [Tau Ceti documentation: `HeckeRing.GL2.Newform.atkinLehnerPseudoEigenvalue`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/AtkinLehner/PseudoEigenvalue.html#HeckeRing.GL2.Newform.atkinLehnerPseudoEigenvalue)
- [Source of `HeckeRing.GL2.Newform.atkinLehnerPseudoEigenvalue` in TauCeti/NumberTheory/ModularForms/AtkinLehner/PseudoEigenvalue.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/AtkinLehner/PseudoEigenvalue.lean#L89)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularForms/STATUS.md)
