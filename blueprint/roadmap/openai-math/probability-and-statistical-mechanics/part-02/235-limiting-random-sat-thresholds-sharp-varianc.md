---
declaration: section
origin: cited
lean: OAI.FixedClauseThreshold.main, OAI.RandomKSAT.sharpness, OAI.RandomKSAT.variance_main, OAI.FixedClauseThreshold.Computability.main
statement: formalized
proof: formalized
---

# 235. Limiting random SAT thresholds, sharp variance and computability

4 manuscripts and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

For random *k*-SAT with independent uniformly signed proper clauses sampled with replacement, proves finite positive limiting thresholds and hitting-time variance $\Theta_k(n)$ for every fixed *k* ≥ 3, and computability of the 3-SAT threshold. We credit Gaia Carenini with priority for resolving the threshold-existence conjecture in her concurrent [ECCC TR26-229](https://eccc.weizmann.ac.il/report/2026/229/), made public October 5, 2026; this family supplies another proof and the sharper variance and computability results.

## A Limiting Satisfiability Threshold for Every Fixed Clause Size

For every fixed integer *k* ≥ 3, random *k*-SAT with independent uniformly signed clauses on distinct variables, sampled with replacement, has a finite positive limiting satisfiability threshold. We credit Gaia Carenini [[5]](https://eccc.weizmann.ac.il/report/2026/229/) with priority for resolving the satisfiability conjecture. This paper gives an alternative proof, using concentration of a capped last satisfiable index and a comparison between different system sizes.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Limiting-Satisfiability-Threshold-for-Every-Fixed-Clause-Size-September-25-2026/article.pdf); the Lean below formalizes results from it.

## Linear Variance of the Random 3-SAT Hitting Time

For random 3-SAT on *n* Boolean variables, with independent uniformly signed clauses on three distinct variables sampled with replacement, we prove that the first unsatisfiable prefix has variance $\Theta(n)$. The upper bound removes the logarithmic loss in the earlier variance estimate; the matching lower bound follows from Wilson's transition-width theorem.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Linear-Variance-of-the-Random-3-SAT-Hitting-Time-October-5-2026/linear-variance-of-the-random-3-sat-hitting-time.pdf).

## Variance of the Random k-SAT Hitting Time

Let $H_{n}$ be the index of the first unsatisfiable prefix in random *k*-SAT on *n* variables, with independent uniformly signed clauses using *k* distinct variables and sampled with replacement. For every fixed *k* ≥ 4, we prove $\mathop{\mathrm{Var}}\nolimits (H_n)=\Theta_k(n)$. For *k* = 3, the variance is bounded below by a positive multiple of *n* and above by a constant multiple of $n\log n$; the companion paper on random 3-SAT sharpens this to $\Theta(n)$. The same upper bounds proved here hold after clipping at any fixed positive multiple of *n*.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Variance-of-the-Random-k-SAT-Hitting-Time-September-27-2026/article.pdf); the Lean below formalizes results from it.

## Computing the Random 3-SAT Threshold

The limiting satisfiability threshold of uniform random 3-SAT is a computable real. We credit Gaia Carenini [[4]](https://eccc.weizmann.ac.il/report/2026/229/) with priority for resolving the satisfiability conjecture, which establishes the threshold's existence. We prove that one finite deterministic machine can approximate it to any prescribed accuracy. A deletion estimate gives explicit lower certificates, while a finite hierarchical approximation of the soft pressure gives upper certificates at every larger rational density. A fair search through these certificates halts without requiring a computable rate of finite-size convergence.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026/article.pdf); the Lean below formalizes results from it.

## The Lean formalization

The random $k$-SAT threshold problem asks whether satisfiability changes at one limiting clause density. The formalization proves that every fixed integer $k\ge3$ has a finite positive threshold $\alpha_k$: for every fixed density $c<\alpha_k$, the satisfiability probability tends to one as the number of variables grows, while for every $c>\alpha_k$ it tends to zero. Clauses use distinct variables with independent uniform signs and are sampled independently with replacement. The statement makes no assertion at the threshold itself.

Let $H_n$ be the first unsatisfiable prefix length in random $k$-SAT with independent uniformly signed clauses on $k$ distinct variables, sampled with replacement. The formalization proves $\mathrm{Var}(H_n)=\Theta_k(n)$ for every fixed $k\ge4$. For $k=3$, it proves a positive linear lower bound and an $O(n\log n)$ upper bound. The same upper bounds hold after clipping at any fixed positive multiple of $n$, and linear lower bounds hold for sufficiently high clipping levels.

The linked supplements prove sharpness of the separate survival-lifetime and clause-replacement estimates used in the argument. They do not show that the logarithmic factor in the $k=3$ variance bound is necessary.

The formalization proves that the limiting threshold $\alpha$ for uniform random $3$-SAT is a computable positive real. Satisfiability tends to one at every fixed density below $\alpha$ and to zero at every fixed density above it. One deterministic machine produces a rational number $q_r$ for every requested precision $r$ with $|q_r-\alpha|\le2^{-r}$. No computable rate of finite-size convergence is assumed in the statement.

## Lean: Limiting satisfiability threshold for every fixed $k\ge3$

Stated in [FixedClauseThreshold.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/FixedClauseThreshold.lean).

```lean
theorem main (k : ℕ) (hk : 3 ≤ k) : HasLimitingThreshold k
```

Proved in [lean/OAI/Probability/RandomSAT/Main.lean, line 122](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/RandomSAT/Main.lean#L122).

## Lean: Sharpness of random $k$-SAT lifetime and replacement bounds

Stated in [SATSharpness.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SATSharpness.lean).

```lean
theorem sharpness (k : ℕ) (hk : 3 ≤ k) :
    (∀ γ D A : ℝ, γ < (k : ℝ) / ((k-1 : ℕ) : ℝ) → 0 < D → 0 < A →
      ∀ N : ℕ, ∃ u : ℕ, N ≤ u ∧ k ≤ u ∧ ∃ S : Finset (Assignment u),
        S.Nonempty ∧ A * (u : ℝ) ^ (-((k-1 : ℕ) : ℝ)) ≤ blockKill u (k-1) S 1 ∧
        D * (blockKill u (k-1) S 1) ^ (-γ) < lifetime u k S) ∧
    (∃ u : ℕ → ℕ, ∃ S : ∀ g, Finset (Assignment (u g)),
      (∀ g, 2 ≤ g → k ≤ u g ∧ (S g).Nonempty) ∧
      Asymptotics.IsEquivalent Filter.atTop
        (fun g => blockKill (u g) (k-1) (S g) 1 - blockKill (u g) k (S g) g)
        (fun g => ((2 : ℝ)^k)⁻¹ * (g : ℝ)^(-((k-1 : ℕ) : ℝ)))) ∧
    (¬ ∃ e : ℕ → ℝ,
      Asymptotics.IsLittleO Filter.atTop e (fun g => (g : ℝ)^(-((k-1 : ℕ) : ℝ))) ∧
      ∀ u, k ≤ u → ∀ S : Finset (Assignment u), S.Nonempty → ∀ g, 2 ≤ g →
        blockKill u (k-1) S 1 - e g ≤ blockKill u k S g)
```

Proved in [lean/OAI/Probability/SATVariance/Sharpness.lean, line 7](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/SATVariance/Sharpness.lean#L7).

## Lean: Variance bounds for the random $k$-SAT hitting time

Stated in [SATVariance.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SATVariance.lean).

```lean
theorem variance_main (k : ℕ) (hk : 3 ≤ k) :
    (∃ C : ℝ, 0 ≤ C ∧ ∀ n : ℕ, k ≤ n →
      variance (H : Stream n k → ℝ) (streamLaw n k) ≤ C * n * ell k n) ∧
    (∀ B : ℝ, 0 < B → ∃ C : ℝ, 0 ≤ C ∧ ∀ n : ℕ, k ≤ n →
      variance (T B : Stream n k → ℝ) (streamLaw n k) ≤ C * n * ell k n) ∧
    (∃ c : ℝ, 0 < c ∧
      (∃ N : ℕ, ∀ n : ℕ, N ≤ n → k ≤ n →
        c * n ≤ variance (H : Stream n k → ℝ) (streamLaw n k)) ∧
      (∀ B : ℝ, U k < B → ∃ N : ℕ, ∀ n : ℕ, N ≤ n → k ≤ n →
        c * n ≤ variance (T B : Stream n k → ℝ) (streamLaw n k)))
```

Proved in [lean/OAI/Probability/SATVariance/Main.lean, line 15](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/SATVariance/Main.lean#L15).

## Lean: Computability of the random $3$-SAT threshold

Stated in [SATComputability.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SATComputability.lean).

```lean
theorem main : MainStatement
```

Proved in [lean/OAI/Probability/SATComputability/Main.lean, line 43](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/SATComputability/Main.lean#L43).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/235.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/235.md)
