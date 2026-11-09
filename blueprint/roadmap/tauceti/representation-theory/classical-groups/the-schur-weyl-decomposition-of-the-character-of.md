---
declaration: theorem
origin: cited
lean: TauCeti.sum_finrank_spechtModule_mul_char_weylRepOfShape_ofPartition, TauCeti.sum_finrank_spechtModule_mul_char_weylFDRepOfShape_ofPartition
statement: formalized
proof: formalized
---

# The Schur-Weyl decomposition of the character of a tensor power

For every `g ∈ GL n k`,
the character of `(kⁿ)^{⊗d}` at `g` is the sum over the partitions `μ` of `d` of the characters of
the Weyl modules `𝕊^μ(kⁿ)` at `g`, each weighted by the dimension `f^μ` of the Specht module
`S^μ`.

```lean
TauCeti.sum_finrank_spechtModule_mul_char_weylRepOfShape_ofPartition.{u} {k : Type u} [Field k]
  [CharZero k] {n : ℕ} (d : ℕ) (g : GL (Fin n) k) :
  ∑ μ,
      ↑(Module.finrank ℚ ↑(TauCeti.spechtModule μ).V) *
        (TauCeti.weylRepOfShape k n (YoungDiagram.ofPartition μ)).character g =
    (TauCeti.tensorPowerRep k n d).character g
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [James's submodule theorem](../symmetric/jamess-submodule-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_finrank_spechtModule_mul_char_weylRepOfShape_ofPartition`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/WeylModule/SchurWeyl.html#TauCeti.sum_finrank_spechtModule_mul_char_weylRepOfShape_ofPartition).

## Other forms

**The Schur-Weyl decomposition of the character of the bundled tensor power.** Formalized in Tau Ceti as [`TauCeti.sum_finrank_spechtModule_mul_char_weylFDRepOfShape_ofPartition`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/WeylModule/SchurWeyl.html#TauCeti.sum_finrank_spechtModule_mul_char_weylFDRepOfShape_ofPartition).

```lean
TauCeti.sum_finrank_spechtModule_mul_char_weylFDRepOfShape_ofPartition.{u} {k : Type u} [Field k]
  [CharZero k] {n : ℕ} (d : ℕ) (g : GL (Fin n) k) :
  ∑ μ,
      ↑(Module.finrank ℚ ↑(TauCeti.spechtModule μ).V) *
        (TauCeti.weylFDRepOfShape k n (YoungDiagram.ofPartition μ)).character g =
    (TauCeti.tensorPowerFDRep k n d).character g
```

## Sources

- [Tau Ceti documentation: `TauCeti.sum_finrank_spechtModule_mul_char_weylRepOfShape_ofPartition`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/WeylModule/SchurWeyl.html#TauCeti.sum_finrank_spechtModule_mul_char_weylRepOfShape_ofPartition)
- [Source of `TauCeti.sum_finrank_spechtModule_mul_char_weylRepOfShape_ofPartition` in TauCeti/RepresentationTheory/ClassicalGroups/WeylModule/SchurWeyl.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/ClassicalGroups/WeylModule/SchurWeyl.lean#L174)
