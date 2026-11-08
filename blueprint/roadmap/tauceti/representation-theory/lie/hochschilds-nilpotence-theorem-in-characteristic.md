---
declaration: theorem
origin: cited
lean: LieSubalgebra.isNilpotent_toEnd_of_isNilpotent_ad_of_isCompl_radical
statement: formalized
proof: formalized
---

# Hochschild's nilpotence theorem in characteristic zero

if the nilradical of a
finite-dimensional Lie algebra `L` acts nilpotently on a finite-dimensional `L`-module `M`, then
so does every `ad`-nilpotent element of `L`. The Lie subalgebra `S` is any Levi complement, that
is, any complement of the solvable radical; the conclusion does not depend on it.

```lean
LieSubalgebra.isNilpotent_toEnd_of_isNilpotent_ad_of_isCompl_radical.{u_1, u_2, u_3} {K : Type u_1}
  {L : Type u_2} {M : Type u_3} [Field K] [CharZero K] [LieRing L] [LieAlgebra K L] [AddCommGroup M]
  [_root_.Module K M] [FiniteDimensional K M] [LieRingModule L M] [LieModule K L M]
  [FiniteDimensional K L] (S : LieSubalgebra K L)
  (hS : IsCompl (↑(LieAlgebra.radical K L)) S.toSubmodule)
  (hM : ∀ n ∈ TauCeti.LieAlgebra.nilradical K L, IsNilpotent ((LieModule.toEnd K L M) n)) {x : L}
  (hx : IsNilpotent ((LieAlgebra.ad K L) x)) : IsNilpotent ((LieModule.toEnd K L M) x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LieSubalgebra.isNilpotent_toEnd_of_isNilpotent_ad_of_isCompl_radical`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Lie/AdNilpotent.html#LieSubalgebra.isNilpotent_toEnd_of_isNilpotent_ad_of_isCompl_radical).

## Sources

- [Tau Ceti documentation: `LieSubalgebra.isNilpotent_toEnd_of_isNilpotent_ad_of_isCompl_radical`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Lie/AdNilpotent.html#LieSubalgebra.isNilpotent_toEnd_of_isNilpotent_ad_of_isCompl_radical)
- [Source of `LieSubalgebra.isNilpotent_toEnd_of_isNilpotent_ad_of_isCompl_radical` in TauCeti/RepresentationTheory/Lie/AdNilpotent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Lie/AdNilpotent.lean#L136)
