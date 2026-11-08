---
declaration: theorem
origin: cited
lean: NumberField.Chebotarev.hasDirichletDensity_primesCongruent, Matrix.exists_int_abs_sum_mul_sub_le, TauCeti.dirichlet_linearForm_infinite, TauCeti.infinite_linearFormApproximations_of_lt_card, TauCeti.Multiquadratic.exists_prime_gt_forall_primeDiscriminantCharFun_eq, Matrix.dirichlet_linearForms, Matrix.dirichlet_linearForms_infinite, TauCeti.infinite_simultaneousApproximationDenominators_inv_card, Real.infinite_setOf_mul_abs_mul_sub_round_le_one
statement: formalized
proof: formalized
---

# Dirichlet's theorem on primes in arithmetic progressions, with Dirichlet density

For
`m ≠ 0` and `a` a unit modulo `m`, the primes of `𝓞 ℚ` whose absolute norm is congruent to `a`
modulo `m` have Dirichlet density `1 / φ(m)`.

```lean
NumberField.Chebotarev.hasDirichletDensity_primesCongruent (m a : ℕ) [NeZero m] (ha : IsUnit ↑a) :
  NumberField.Set.HasDirichletDensity {𝔭 | Ideal.absNorm 𝔭.asIdeal % m = a % m} (1 / ↑m.totient)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A one-sided Abel bound](../arithmetic-dirichlet-series-and-tauberian-method/part-01/a-one-sided-abel-bound.md)
- [The analytic Euler product](../arithmetic-dirichlet-series-and-tauberian-method/part-01/the-analytic-euler-product.md)
- [Boundary data for the prime Dirichlet series of `S`](../arithmetic-dirichlet-series-and-tauberian-method/part-01/boundary-data-for-the-prime-dirichlet-series-of.md)
- [Minkowski's convex body theorem for the integer lattice](../counting-totally-ramified-extensions-of-a-local/part-01/minkowskis-convex-body-theorem-for-the-integer-l.md)
- [The prime ideal theorem](../arithmetic-dirichlet-series-and-tauberian-method/part-01/the-prime-ideal-theorem.md)
- [Prime-number-theorem transfer from exact boundary data](../arithmetic-dirichlet-series-and-tauberian-method/part-01/prime-number-theorem-transfer-from-exact-boundar.md)

## Lean

Formalized in Tau Ceti as [`NumberField.Chebotarev.hasDirichletDensity_primesCongruent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/Density/PrimesCongruent.html#NumberField.Chebotarev.hasDirichletDensity_primesCongruent).

## Other forms

**Dirichlet's theorem for linear forms, with general bounds.** Formalized in Tau Ceti as [`Matrix.exists_int_abs_sum_mul_sub_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Dirichlet.html#Matrix.exists_int_abs_sum_mul_sub_le).

```lean
Matrix.exists_int_abs_sum_mul_sub_le.{u_1, u_2} {ι : Type u_1} {κ : Type u_2} [Fintype ι]
  [Fintype κ] [Nonempty κ] (A : Matrix ι κ ℝ) {P δ : ℝ} (hP : 0 ≤ P) (hδ₀ : 0 ≤ δ) (hδ₁ : δ < 1)
  (h : 1 ≤ P ^ Fintype.card κ * δ ^ Fintype.card ι) :
  ∃ y x, y ≠ 0 ∧ (∀ (j : κ), |↑(y j)| ≤ P) ∧ ∀ (i : ι), |∑ j, A i j * ↑(y j) - ↑(x i)| ≤ δ
```

**Dirichlet's theorem for one linear form, infinitely many solutions.** Formalized in Tau Ceti as [`TauCeti.dirichlet_linearForm_infinite`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Dirichlet.html#TauCeti.dirichlet_linearForm_infinite).

```lean
TauCeti.dirichlet_linearForm_infinite.{u_2} {κ : Type u_2} [Fintype κ] [Nonempty κ] (α : κ → ℝ)
  (hα : ∀ (y : κ → ℤ), (∃ k, ∑ j, α j * ↑(y j) = ↑k) → y = 0) :
  {p | p.2 ≠ 0 ∧ |∑ j, α j * ↑(p.2 j) - ↑p.1| ≤ ‖p.2‖ ^ (-↑(Fintype.card κ))}.Infinite
```

**Dirichlet's theorem for one linear form, infinitely many solutions.** Formalized in Tau Ceti as [`TauCeti.infinite_linearFormApproximations_of_lt_card`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/LinearFormExponent.html#TauCeti.infinite_linearFormApproximations_of_lt_card).

```lean
TauCeti.infinite_linearFormApproximations_of_lt_card.{u_1} {ι : Type u_1} [Fintype ι] [Nonempty ι]
  {θ : ι → ℝ} (hθ : ∀ (x : ℤ × (ι → ℤ)), ↑x.1 + ∑ i, ↑(x.2 i) * θ i = 0 → x = 0) {w : ℝ}
  (hw : w < ↑(Fintype.card ι)) : (TauCeti.linearFormApproximations θ w).Infinite
```

**Dirichlet's theorem for prime-discriminant characters.** Formalized in Tau Ceti as [`TauCeti.Multiquadratic.exists_prime_gt_forall_primeDiscriminantCharFun_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Legendre/PrimeDiscriminant/Dirichlet/Basic.html#TauCeti.Multiquadratic.exists_prime_gt_forall_primeDiscriminantCharFun_eq).

```lean
TauCeti.Multiquadratic.exists_prime_gt_forall_primeDiscriminantCharFun_eq {s : Finset ℤ}
  (hs : ∀ P ∈ s, TauCeti.Multiquadratic.IsPrimeDiscriminant P)
  (heven :
    ∀ P ∈ s,
      ∀ Q ∈ s,
        TauCeti.Multiquadratic.IsEvenPrimeDiscriminant P →
          TauCeti.Multiquadratic.IsEvenPrimeDiscriminant Q → P = Q)
  (ε : ℤ → ℤˣ) (N : ℕ) :
  ∃ q,
    N < q ∧
      Nat.Prime q ∧ q ≠ 2 ∧ ∀ P ∈ s, TauCeti.Multiquadratic.primeDiscriminantCharFun P ↑q = ↑(ε P)
```

**Dirichlet's theorem for systems of linear forms.** Formalized in Tau Ceti as [`Matrix.dirichlet_linearForms`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Dirichlet.html#Matrix.dirichlet_linearForms).

```lean
Matrix.dirichlet_linearForms.{u_1, u_2} {ι : Type u_1} {κ : Type u_2} [Fintype ι] [Fintype κ]
  [Nonempty ι] [Nonempty κ] (A : Matrix ι κ ℝ) {Q : ℝ} (hQ : 1 < Q) :
  ∃ y x,
    y ≠ 0 ∧
      (∀ (j : κ), |↑(y j)| ≤ Q) ∧
        ∀ (i : ι), |∑ j, A i j * ↑(y j) - ↑(x i)| ≤ Q ^ (-↑(Fintype.card κ) / ↑(Fintype.card ι))
```

**Dirichlet's theorem for systems of linear forms, infinitely many solutions.** Formalized in Tau Ceti as [`Matrix.dirichlet_linearForms_infinite`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Dirichlet.html#Matrix.dirichlet_linearForms_infinite).

```lean
Matrix.dirichlet_linearForms_infinite.{u_1, u_2} {ι : Type u_1} {κ : Type u_2} [Fintype ι]
  [Fintype κ] [Nonempty κ] (A : Matrix ι κ ℝ)
  (hA : ∀ (y : κ → ℤ), (∀ (i : ι), ∃ k, ∑ j, A i j * ↑(y j) = ↑k) → y = 0) :
  {p |
      p.1 ≠ 0 ∧
        ∀ (i : ι),
          |∑ j, A i j * ↑(p.1 j) - ↑(p.2 i)| ≤
            ‖p.1‖ ^ (-↑(Fintype.card κ) / ↑(Fintype.card ι))}.Infinite
```

**Dirichlet's theorem, infinitely many denominators.** Formalized in Tau Ceti as [`TauCeti.infinite_simultaneousApproximationDenominators_inv_card`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/SimultaneousExponent.html#TauCeti.infinite_simultaneousApproximationDenominators_inv_card).

```lean
TauCeti.infinite_simultaneousApproximationDenominators_inv_card.{u_1} {ι : Type u_1} [Fintype ι]
  (θ : ι → ℝ) : (TauCeti.simultaneousApproximationDenominators θ (↑(Fintype.card ι))⁻¹).Infinite
```

**Dirichlet's theorem, nearest-integer form.** Formalized in Tau Ceti as [`Real.infinite_setOf_mul_abs_mul_sub_round_le_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Dirichlet.html#Real.infinite_setOf_mul_abs_mul_sub_round_le_one).

```lean
Real.infinite_setOf_mul_abs_mul_sub_round_le_one (α : ℝ) :
  {q | 0 < q ∧ ↑q * |↑q * α - ↑(round (↑q * α))| ≤ 1}.Infinite
```

## Sources

- [Tau Ceti documentation: `NumberField.Chebotarev.hasDirichletDensity_primesCongruent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/Density/PrimesCongruent.html#NumberField.Chebotarev.hasDirichletDensity_primesCongruent)
- [Source of `NumberField.Chebotarev.hasDirichletDensity_primesCongruent` in TauCeti/NumberTheory/Chebotarev/Density/PrimesCongruent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Chebotarev/Density/PrimesCongruent.lean#L116)
- [Tau Ceti roadmap status: The Chebotarev density theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/Chebotarev/STATUS.md)
