---
declaration: theorem
origin: cited
lean: RootPairing.sum_range_root_pow_apply_eq_nsmul
statement: formalized
proof: formalized
---

# Full-period sums

If `σᵐ` fixes `i`, then summing the roots `σᵏ αᵢ` over `k < m`
counts every root of the orbit `m / d` times, where `d` is the size of the orbit.

```lean
RootPairing.sum_range_root_pow_apply_eq_nsmul.{u_1, u_2, u_3, u_4} {ι : Type u_1} {R : Type u_2}
  {M : Type u_3} {N : Type u_4} [CommRing R] [AddCommGroup M] [_root_.Module R M] [AddCommGroup N]
  [_root_.Module R N] {P : RootPairing ι R M N} [Finite ι] {σ : P.Aut} {i : ι} {m : ℕ}
  (hm : ((↑σ).indexEquiv ^ m) i = i) :
  ∑ k ∈ Finset.range m, P.root (((↑σ).indexEquiv ^ k) i) =
    (m / (P.orbitIndices σ i).card) • P.orbitSum σ i
```

## Depends on

- [RootPairing.orbitSum](rootpairing-orbitsum.md)

## Lean

Formalized in Tau Ceti as [`RootPairing.sum_range_root_pow_apply_eq_nsmul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/OrbitSum.html#RootPairing.sum_range_root_pow_apply_eq_nsmul).

## Sources

- [Tau Ceti documentation: `RootPairing.sum_range_root_pow_apply_eq_nsmul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/OrbitSum.html#RootPairing.sum_range_root_pow_apply_eq_nsmul)
- [Source of `RootPairing.sum_range_root_pow_apply_eq_nsmul` in TauCeti/LinearAlgebra/RootSystem/OrbitSum.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/RootSystem/OrbitSum.lean#L196)
- [Tau Ceti roadmap status: Root systems, integral dominance and finite diagram folding, part II](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RootSystemsPartII/STATUS.md)
