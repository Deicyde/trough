---
declaration: theorem
origin: cited
lean: TauCeti.isSuperfluous_smul_top_of_isNilpotent
statement: formalized
proof: formalized
---

# Nakayama's lemma for a nilpotent ideal

If `I` is a nilpotent ideal then `I • M` is
superfluous in `M`.

Unlike `TauCeti.isSuperfluous_jacobson`, which asks the submodule lattice of `M` to be coatomic
(for instance `M` finitely generated) and takes the radical of `M`, nilpotence of `I` buys the
conclusion for an arbitrary module: a submodule `K` with `I • M ⊔ K = ⊤` absorbs `I ^ k • M` into
`I ^ (k + 1) • M` for every `k`, and a power of `I` vanishes.

```lean
TauCeti.isSuperfluous_smul_top_of_isNilpotent.{u, v} {R : Type u} {M : Type v} [Semiring R]
  [AddCommMonoid M] [_root_.Module R M] {I : Ideal R} (hI : IsNilpotent I) :
  TauCeti.IsSuperfluous (I • ⊤)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isSuperfluous_smul_top_of_isNilpotent`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/Submodule/Superfluous.html#TauCeti.isSuperfluous_smul_top_of_isNilpotent).

## Sources

- [Tau Ceti documentation: `TauCeti.isSuperfluous_smul_top_of_isNilpotent`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/Submodule/Superfluous.html#TauCeti.isSuperfluous_smul_top_of_isNilpotent)
- [Source of `TauCeti.isSuperfluous_smul_top_of_isNilpotent` in TauCeti/Algebra/Module/Submodule/Superfluous.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Module/Submodule/Superfluous.lean#L163)
