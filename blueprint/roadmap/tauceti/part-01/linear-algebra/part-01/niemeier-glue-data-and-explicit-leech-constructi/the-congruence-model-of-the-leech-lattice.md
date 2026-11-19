---
declaration: theorem
origin: cited
lean: TauCeti.mem_leechLattice_carrier_iff_exists
statement: formalized
proof: formalized
---

# The congruence model of the Leech lattice

A vector `x` lies in the Leech lattice exactly
when `x = a / 2` for an integer vector `a = 2b + m 𝟙` with `m ∈ {0, 1}`, `b` reducing to a Golay
codeword modulo two, and `∑ aᵢ ≡ 4m (mod 8)`.

```lean
TauCeti.mem_leechLattice_carrier_iff_exists (x : Fin 24 → ℚ) :
  x ∈ TauCeti.leechLattice.carrier ↔
    ∃ m,
      (m = 0 ∨ m = 1) ∧
        ∃ b,
          (fun i => ↑(b i)) ∈ TauCeti.BinaryGolay.code ∧
            ∑ i, (2 * b i + m) ≡ 4 * m [ZMOD 8] ∧ x = fun i => ↑(2 * b i + m) / 2
```

## Depends on

- [TauCeti.ConstructionA.lattice](../algebraic-codes-and-code-lattice-constructions/tauceti-constructiona-lattice.md)
- [TauCeti.FiniteQuadraticModule](../../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice-discriminantquadraticmod.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mem_leechLattice_carrier_iff_exists`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/Leech/Minimum.html#TauCeti.mem_leechLattice_carrier_iff_exists).

## Sources

- [Tau Ceti documentation: `TauCeti.mem_leechLattice_carrier_iff_exists`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/Leech/Minimum.html#TauCeti.mem_leechLattice_carrier_iff_exists)
- [Source of `TauCeti.mem_leechLattice_carrier_iff_exists` in TauCeti/LinearAlgebra/IntegralLattice/Rank24/Leech/Minimum.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/IntegralLattice/Rank24/Leech/Minimum.lean#L95)
- [Tau Ceti roadmap status: Niemeier glue data and explicit Leech constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Rank24LatticeConstructions/STATUS.md)
