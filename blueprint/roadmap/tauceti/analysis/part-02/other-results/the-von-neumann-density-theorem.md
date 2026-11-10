---
declaration: theorem
origin: cited
lean: StarSubalgebra.exists_forall_norm_sub_apply_lt_of_mem_centralizer_centralizer, VonNeumannAlgebra.exists_forall_norm_sub_apply_lt_of_mem_adjoin, StarSubalgebra.apply_mem_closure_of_mem_centralizer_centralizer
statement: formalized
proof: formalized
---

# The von Neumann density theorem

An operator `x` in the double commutant of a unital star
subalgebra `S` of the bounded operators on a Hilbert space is a strong-operator limit of elements
of `S`: for every finite family of vectors `v i` and every `ε > 0` there is `s ∈ S` with
`‖x (v i) - s (v i)‖ < ε` for all `i`.

```lean
StarSubalgebra.exists_forall_norm_sub_apply_lt_of_mem_centralizer_centralizer.{u_1, u_2, u_3}
  {𝕜 : Type u_1} {H : Type u_2} [RCLike 𝕜] [NormedAddCommGroup H] [InnerProductSpace 𝕜 H]
  [CompleteSpace H] (S : StarSubalgebra 𝕜 (H →L[𝕜] H)) {x : H →L[𝕜] H}
  (hx : x ∈ (↑S).centralizer.centralizer) {ι : Type u_3} [Finite ι] (v : ι → H) {ε : ℝ}
  (hε : 0 < ε) : ∃ s ∈ S, ∀ (i : ι), ‖x (v i) - s (v i)‖ < ε
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`StarSubalgebra.exists_forall_norm_sub_apply_lt_of_mem_centralizer_centralizer`](https://taucetiproject.org/docs/TauCeti/Analysis/VonNeumannAlgebra/Density.html#StarSubalgebra.exists_forall_norm_sub_apply_lt_of_mem_centralizer_centralizer).

## Other forms

**The von Neumann density theorem for a generated von Neumann algebra.** Formalized in Tau Ceti as [`VonNeumannAlgebra.exists_forall_norm_sub_apply_lt_of_mem_adjoin`](https://taucetiproject.org/docs/TauCeti/Analysis/VonNeumannAlgebra/Density.html#VonNeumannAlgebra.exists_forall_norm_sub_apply_lt_of_mem_adjoin).

```lean
VonNeumannAlgebra.exists_forall_norm_sub_apply_lt_of_mem_adjoin.{u_1, u_2} {H : Type u_1}
  [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H] {s : Set (H →L[ℂ] H)}
  {x : H →L[ℂ] H} (hx : x ∈ VonNeumannAlgebra.adjoin s) {ι : Type u_2} [Finite ι] (v : ι → H)
  {ε : ℝ} (hε : 0 < ε) : ∃ t ∈ StarAlgebra.adjoin ℂ s, ∀ (i : ι), ‖x (v i) - t (v i)‖ < ε
```

**The von Neumann density theorem for one vector.** Formalized in Tau Ceti as [`StarSubalgebra.apply_mem_closure_of_mem_centralizer_centralizer`](https://taucetiproject.org/docs/TauCeti/Analysis/VonNeumannAlgebra/Density.html#StarSubalgebra.apply_mem_closure_of_mem_centralizer_centralizer).

```lean
StarSubalgebra.apply_mem_closure_of_mem_centralizer_centralizer.{u_1, u_2} {𝕜 : Type u_1}
  {H : Type u_2} [RCLike 𝕜] [NormedAddCommGroup H] [InnerProductSpace 𝕜 H] [CompleteSpace H]
  (S : StarSubalgebra 𝕜 (H →L[𝕜] H)) {x : H →L[𝕜] H} (hx : x ∈ (↑S).centralizer.centralizer)
  (v : H) : x v ∈ closure ((fun s => s v) '' ↑S)
```

## Sources

- [Tau Ceti documentation: `StarSubalgebra.exists_forall_norm_sub_apply_lt_of_mem_centralizer_centralizer`](https://taucetiproject.org/docs/TauCeti/Analysis/VonNeumannAlgebra/Density.html#StarSubalgebra.exists_forall_norm_sub_apply_lt_of_mem_centralizer_centralizer)
- [Source of `StarSubalgebra.exists_forall_norm_sub_apply_lt_of_mem_centralizer_centralizer` in TauCeti/Analysis/VonNeumannAlgebra/Density.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/VonNeumannAlgebra/Density.lean#L124)
