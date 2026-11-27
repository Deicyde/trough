---
declaration: theorem
origin: cited
lean: ChebyshevBias.littlewood_mod_four_sign_changes, ChebyshevBias.knapowski_turan_natural_density_false, ChebyshevBias.rubinstein_sarnak_unconditional_chebyshev_bias, ChebyshevBias.rubinstein_sarnak_unconditional_chebyshev_bias.variants.general_modulus
statement: formalized
---

# Chebyshev's bias

> Let $\pi(n; q, r)$ (`Nat.primeCountingMod n q r`) count primes $p \le n$ satisfying
> $p \equiv r \pmod q$. Pafnuty Chebyshev (1853) noted that $\pi(n; 4, 3)$ usually exceeds
> $\pi(n; 4, 1)$. John E. Littlewood (1914) established that $\pi(n; 4, 3) - \pi(n; 4, 1)$ switches
> sign infinitely often (first becoming negative at $n = 26861$). Jerzy Kaczorowski (1995) disproved
> Stanisław Knapowski and Pál Turán's (1962) conjecture that
> $\{n \in \mathbb{N} : \pi(n; 4, 3) > \pi(n; 4, 1)\}$ has natural density $1$ assuming GRH for
> $L(s, \chi_4)$, whereas Kevin Ford, Sergei Konyagin, and Youness Lamzouri (2013) showed that
> hypothetical off-critical zeros could force natural density $0$ or $1$. Assuming GRH and linear
> independence of positive ordinates of Dirichlet $L$-zeros, Michael Rubinstein and Peter Sarnak
> (1994) showed this set has logarithmic density $\delta_{4; 3, 1} \approx 0.9959 \in (1/2, 1)$, and
> more generally that coprime quadratic nonresidues modulo $q \ge 3$ lead coprime quadratic residues
> with logarithmic density in $(1/2, 1)$; proving this unconditionally remains open.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Chebyshev%27s_bias)
> - J. E. Littlewood, *Sur la distribution des nombres premiers*, C. R. Acad. Sci. **158**
>   (1914), 1869–1872.
> - M. Rubinstein and P. Sarnak, *Chebyshev's bias*, Experiment. Math. **3** (1994), 173–197.
> - J. Kaczorowski, *On the distribution of primes ($\bmod\, 4$)*, Analysis **15** (1995), no. 2,
>   159–171.
> - K. Ford, S. Konyagin, and Y. Lamzouri, *The prime number race and zeros of Dirichlet
>   $L$-functions off the critical line. III*, Quart. J. Math. **64** (2013), no. 4, 1091–1098
>   (`arXiv:1204.6715`).

*Quoted from [FormalConjectures/Wikipedia/ChebyshevBias.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ChebyshevBias.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 2 open and 2 solved. It also has 2 test statements, counted here but not shown.

## `ChebyshevBias.littlewood_mod_four_sign_changes`

Solved: stated here without proof.

> Littlewood's oscillation theorem (1914): both $\pi(n; 4, 3) > \pi(n; 4, 1)$ and
> $\pi(n; 4, 1) > \pi(n; 4, 3)$ hold for infinitely many $n \in \mathbb{N}$.

```lean
theorem littlewood_mod_four_sign_changes :
    chebyshevModFourLeadSet.Infinite ∧
      {n : ℕ | n.primeCountingMod 4 3 < n.primeCountingMod 4 1}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ChebyshevBias.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ChebyshevBias.lean#L73).

## `ChebyshevBias.knapowski_turan_natural_density_false`

Solved: stated here without proof.

> Conditional refutation of the Knapowski–Turán natural-density conjecture (Kaczorowski 1995):
> assuming the Generalized Riemann Hypothesis for $L(s, \chi_4)$, the set of $n \in \mathbb{N}$ with
> $\pi(n; 4, 3) > \pi(n; 4, 1)$ does not have natural density $1$. (Ford, Konyagin, and Lamzouri,
> `arXiv:1204.6715`, showed that hypothetical off-critical zeros could make the natural density $0$
> or $1$.)

```lean
theorem knapowski_turan_natural_density_false
    (hGRH : ∀ s : ℂ, 0 < s.re → s.re < 1 →
      DirichletCharacter.LFunction (ZMod.χ₄.ringHomComp (Int.castRingHom ℂ)) s = 0 →
      s.re = 1 / 2) :
    ¬ chebyshevModFourLeadSet.HasDensity 1
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ChebyshevBias.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ChebyshevBias.lean#L84).

## `ChebyshevBias.rubinstein_sarnak_unconditional_chebyshev_bias`

Open: stated without proof.

> Unconditional Rubinstein–Sarnak Chebyshev bias conjecture modulo $4$ (obtained by removing GRH
> and the linear independence hypothesis LI from Rubinstein and Sarnak's conditional theorem): the
> set of $n \in \mathbb{N}$ satisfying $\pi(n; 4, 3) > \pi(n; 4, 1)$ admits a logarithmic density
> $\delta \in (1/2, 1)$.

```lean
theorem rubinstein_sarnak_unconditional_chebyshev_bias :
    ∃ δ : ℝ, (1 : ℝ) / 2 < δ ∧ δ < 1 ∧ Set.HasLogDensity chebyshevModFourLeadSet δ
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ChebyshevBias.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ChebyshevBias.lean#L96).

## `ChebyshevBias.rubinstein_sarnak_unconditional_chebyshev_bias.variants.general_modulus`

Open: stated without proof.

> Unconditional general-modulus Chebyshev bias conjecture (obtained by removing GRH and the
> linear independence hypothesis LI from Rubinstein and Sarnak's conditional theorem): for any
> modulus $q \ge 3$ and integers $a, b$ coprime to $q$ such that $a$ is a quadratic residue modulo
> $q$ and $b$ is a quadratic nonresidue modulo $q$, the set
> $\{n \in \mathbb{N} : \pi(n; q, b) > \pi(n; q, a)\}$ admits a logarithmic density
> $\delta \in (1/2, 1)$.

```lean
theorem rubinstein_sarnak_unconditional_chebyshev_bias.variants.general_modulus
    (q a b : ℕ) (hq : 3 ≤ q) (ha : a.Coprime q) (hb : b.Coprime q)
    (hres : IsSquare (a : ZMod q)) (hnonres : ¬ IsSquare (b : ZMod q)) :
    ∃ δ : ℝ, (1 : ℝ) / 2 < δ ∧ δ < 1 ∧
      Set.HasLogDensity {n : ℕ | n.primeCountingMod q a < n.primeCountingMod q b} δ
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ChebyshevBias.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ChebyshevBias.lean#L107).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/ChebyshevBias.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ChebyshevBias.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Chebyshev%27s_bias)
