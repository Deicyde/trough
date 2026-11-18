---
declaration: theorem
origin: cited
lean: TauCeti.AInfinityAlgebra.mem_tripleMasseyProduct_iff_sub_minimalModel_m_three_mem
statement: formalized
proof: formalized
---

# The triple Massey product is a coset of the minimal-model ternary operation

if `x y = 0`
and `y z = 0`, then `w` lies in `⟨x, y, z⟩` exactly when `w - m₃^H (x, y, z)` lies in the
indeterminacy `τx · H + H · z`.

```lean
TauCeti.AInfinityAlgebra.mem_tripleMasseyProduct_iff_sub_minimalModel_m_three_mem.{uK, uA}
  {K : Type uK} {A : Type uA} [Field K] [AddCommGroup A] [_root_.Module K A]
  (𝒜 : TauCeti.AInfinityAlgebra K A) {x y z w : 𝒜.Cohomology} (hxy : x * y = 0) (hyz : y * z = 0) :
  w ∈ 𝒜.tripleMasseyProduct x y z ↔
    w - (𝒜.minimalModel.m 3) ![x, y, z] ∈ 𝒜.tripleMasseyIndeterminacy x z
```

## Depends on

- [TauCeti.AInfinityAlgebra.minimalModel](tauceti-ainfinityalgebra-minimalmodel.md)

## Proof depends on

- [TauCeti.AInfinityAlgebra.transfer](tauceti-ainfinityalgebra-transfer.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AInfinityAlgebra.mem_tripleMasseyProduct_iff_sub_minimalModel_m_three_mem`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Massey.html#TauCeti.AInfinityAlgebra.mem_tripleMasseyProduct_iff_sub_minimalModel_m_three_mem).

## Sources

- [Tau Ceti documentation: `TauCeti.AInfinityAlgebra.mem_tripleMasseyProduct_iff_sub_minimalModel_m_three_mem`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Massey.html#TauCeti.AInfinityAlgebra.mem_tripleMasseyProduct_iff_sub_minimalModel_m_three_mem)
- [Source of `TauCeti.AInfinityAlgebra.mem_tripleMasseyProduct_iff_sub_minimalModel_m_three_mem` in TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Massey.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Massey.lean#L105)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DGAInfinity/STATUS.md)
