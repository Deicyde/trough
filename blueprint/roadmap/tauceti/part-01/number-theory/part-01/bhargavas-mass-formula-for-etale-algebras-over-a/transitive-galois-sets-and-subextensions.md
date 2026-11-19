---
declaration: theorem
origin: cited
lean: TauCeti.GaloisSet.tsum_isTransitive
statement: formalized
proof: formalized
---

# Transitive Galois sets and subextensions

Summed over the transitive labelled Galois sets
of size `n`, any weight `g` of the fixed field of the stabilizer of a label `i` is `(n - 1)!`
times the sum of `g` over the subextensions of `SeparableClosure K` of degree `n`: each such
subextension is the fixed field for exactly `(n - 1)!` of them.

```lean
TauCeti.GaloisSet.tsum_isTransitive.{u} {K : Type u} [Field K] {n : ℕ} (i : Fin n)
  (g : IntermediateField K (SeparableClosure K) → ENNReal) :
  ∑' (ρ : { ρ // ρ.IsTransitive }),
      g (IntermediateField.fixedField (MulAction.stabilizer Gal(SeparableClosure K/K) i)) =
    ↑(n - 1).factorial * ∑' (L : { L // Module.finrank K ↥L = n }), g ↑L
```

## Depends on

- [TauCeti.GaloisSet](tauceti-galoisset.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GaloisSet.tsum_isTransitive`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Galois/GaloisSet/Basic.html#TauCeti.GaloisSet.tsum_isTransitive).

## Sources

- [Tau Ceti documentation: `TauCeti.GaloisSet.tsum_isTransitive`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Galois/GaloisSet/Basic.html#TauCeti.GaloisSet.tsum_isTransitive)
- [Source of `TauCeti.GaloisSet.tsum_isTransitive` in TauCeti/FieldTheory/Galois/GaloisSet/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/FieldTheory/Galois/GaloisSet/Basic.lean#L353)
- [Tau Ceti roadmap status: Bhargava's mass formula for étale algebras over a local field](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EtaleMassFormula/STATUS.md)
