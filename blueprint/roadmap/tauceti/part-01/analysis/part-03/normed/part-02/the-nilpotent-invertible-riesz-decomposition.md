---
declaration: theorem
origin: cited
lean: IsCompactOperator.exists_stable_ker_range_restrictions_sub_smul
statement: formalized
proof: formalized
---

# The nilpotent/invertible Riesz decomposition

For a compact operator and a nonzero
scalar, the stable kernel and range of the shifted operator are topological complements.
The kernel is finite dimensional and the shifted restriction to it is nilpotent; the
restriction to the range is invertible as a bounded operator. The stable exponent also
annihilates the kernel restriction. Neither a nonzero-space nor an eigenvalue hypothesis
is required.

```lean
IsCompactOperator.exists_stable_ker_range_restrictions_sub_smul.{u_1, u_2} {𝕜 : Type u_1}
  {X : Type u_2} [NontriviallyNormedField 𝕜] [CompleteSpace 𝕜] [IsRCLikeNormedField 𝕜]
  [NormedAddCommGroup X] [NormedSpace 𝕜 X] [CompleteSpace X] {K : X →L[𝕜] X}
  (hK : IsCompactOperator ⇑K) {μ : 𝕜} (hμ : μ ≠ 0) :
  ∃ p,
    have A := K - μ • 1;
    have f := ↑A;
    let M := (f ^ p).ker;
    let N := (f ^ p).range;
    (∀ (n : ℕ), p ≤ n → (f ^ n).ker = M ∧ (f ^ n).range = N) ∧
      FiniteDimensional 𝕜 ↥M ∧
        Submodule.IsTopCompl M N ∧
          ∃ (hM : ∀ x ∈ M, A x ∈ M) (hN : ∀ x ∈ N, A x ∈ N),
            A.restrict hM ^ p = 0 ∧ IsUnit (A.restrict hN)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Riesz's lemma, translated form](rieszs-lemma-translated-form.md)

## Lean

Formalized in Tau Ceti as [`IsCompactOperator.exists_stable_ker_range_restrictions_sub_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Compact/Restriction.html#IsCompactOperator.exists_stable_ker_range_restrictions_sub_smul).

## Sources

- [Tau Ceti documentation: `IsCompactOperator.exists_stable_ker_range_restrictions_sub_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Compact/Restriction.html#IsCompactOperator.exists_stable_ker_range_restrictions_sub_smul)
- [Source of `IsCompactOperator.exists_stable_ker_range_restrictions_sub_smul` in TauCeti/Analysis/Normed/Operator/Compact/Restriction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Operator/Compact/Restriction.lean#L42)
