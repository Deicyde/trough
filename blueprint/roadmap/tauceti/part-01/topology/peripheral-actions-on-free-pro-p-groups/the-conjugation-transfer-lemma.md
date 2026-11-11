---
declaration: theorem
origin: cited
lean: TauCeti.map_conj_eq_conj_of_map_eq_conj
statement: formalized
proof: formalized
---

# The conjugation-transfer lemma

Let `φ` be an endomorphism of a group `G` and `pow` a self
map of `G` commuting with conjugation by `q` at `x`. If `φ x = c⁻¹ * pow x * c`, then the image of
the conjugate `q * x * q⁻¹` is the conjugate of `pow (q * x * q⁻¹)` by `q * c * (φ q)⁻¹`.

```lean
TauCeti.map_conj_eq_conj_of_map_eq_conj.{u_1, u_2} {G : Type u_1} {M : Type u_2} [Group G]
  [FunLike M G G] [MonoidHomClass M G G] (φ : M) (pow : G → G) {x c q : G}
  (hpow : pow (q * x * q⁻¹) = q * pow x * q⁻¹) (hx : φ x = c⁻¹ * pow x * c) :
  φ (q * x * q⁻¹) = (q * c * (φ q)⁻¹)⁻¹ * pow (q * x * q⁻¹) * (q * c * (φ q)⁻¹)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.map_conj_eq_conj_of_map_eq_conj`](https://taucetiproject.org/docs/TauCeti/GroupTheory/ConjugationTransfer.html#TauCeti.map_conj_eq_conj_of_map_eq_conj).

## Sources

- [Tau Ceti documentation: `TauCeti.map_conj_eq_conj_of_map_eq_conj`](https://taucetiproject.org/docs/TauCeti/GroupTheory/ConjugationTransfer.html#TauCeti.map_conj_eq_conj_of_map_eq_conj)
- [Source of `TauCeti.map_conj_eq_conj_of_map_eq_conj` in TauCeti/GroupTheory/ConjugationTransfer.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/ConjugationTransfer.lean#L37)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/PeripheralActions/STATUS.md)
