---
declaration: theorem
origin: cited
lean: TauCeti.expect_norm_sum_smul_le, TauCeti.rademacherMoment_smul_le
statement: formalized
proof: formalized
---

# Kahane–Khintchine contraction principle in `L¹`

if `∀ i, |α i| ≤ M`, then
`𝔼_ε ‖∑ i, εᵢ (αᵢ xᵢ)‖ ≤ M * 𝔼_ε ‖∑ i, εᵢ xᵢ‖`.

```lean
TauCeti.expect_norm_sum_smul_le.{u_1, u_2} {ι : Type u_1} {E : Type u_2} [Fintype ι] [DecidableEq ι]
  [SeminormedAddCommGroup E] [NormedSpace ℝ E] {α : ι → ℝ} {M : ℝ} (hα : ∀ (i : ι), |α i| ≤ M)
  (x : ι → E) :
  (Finset.univ.expect fun ε => ‖∑ i, ε i • α i • x i‖) ≤
    M * Finset.univ.expect fun ε => ‖∑ i, ε i • x i‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Convex Rademacher contraction principle](../part-01/convex-rademacher-contraction-principle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.expect_norm_sum_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/Contraction.html#TauCeti.expect_norm_sum_smul_le).

## Other forms

**Kahane–Khintchine contraction principle for `K_p` (`1 ≤ p`).** Formalized in Tau Ceti as [`TauCeti.rademacherMoment_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/Contraction.html#TauCeti.rademacherMoment_smul_le).

```lean
TauCeti.rademacherMoment_smul_le.{u_1, u_2} {ι : Type u_1} {E : Type u_2} [Fintype ι]
  [DecidableEq ι] [SeminormedAddCommGroup E] [NormedSpace ℝ E] {p : ℝ} (hp : 1 ≤ p) {α : ι → ℝ}
  {M : ℝ} (hα : ∀ (i : ι), |α i| ≤ M) (x : ι → E) :
  (TauCeti.rademacherMoment p fun i => α i • x i) ≤ M * TauCeti.rademacherMoment p x
```

## Sources

- [Tau Ceti documentation: `TauCeti.expect_norm_sum_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/Contraction.html#TauCeti.expect_norm_sum_smul_le)
- [Source of `TauCeti.expect_norm_sum_smul_le` in TauCeti/Analysis/Normed/Module/RademacherSum/Contraction.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Module/RademacherSum/Contraction.lean#L176)
