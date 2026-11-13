---
declaration: theorem
origin: cited
lean: Transcendental.exp_add_pi_transcendental, Transcendental.exp_mul_pi_transcendental, Transcendental.exp_pow_pi_sq_transcendental, Transcendental.exp_exp_transcendental, Transcendental.pi_pow_exp_transcendental, Transcendental.pi_pow_sqrt_two_transcendental, Transcendental.pi_pow_pi_transcendental, Transcendental.pi_pow_pi_pow_pi_transcendental, Transcendental.pi_pow_pi_pow_pi_pow_pi_transcendental, Transcendental.pi_pow_pi_pow_pi_pow_pi_not_integer, Transcendental.rlog_pi_transcendental, Transcendental.rlog_rlog_two_transcendental, Transcendental.sin_exp_transcendental, Transcendental.exp_add_pi_or_exp_add_mul_transcendental, Transcendental.transcendental_eulerMascheroniConstant_or_gompertzConstant, Transcendental.transcendental_catalanConstant, Transcendental.transcendental_gompertzConstant, Transcendental.transcendental_gamma_one_div_two, Transcendental.transcendental_gamma_one_div_three, Transcendental.transcendental_gamma_one_div_four, Transcendental.transcendental_gamma_one_div_six, Transcendental.transcendental_gamma_one_div
statement: formalized
---

# Open questions on transcendence of numbers

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Transcendental_number)

*Quoted from [FormalConjectures/Wikipedia/Transcendental.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 22 research or textbook statements: 16 open, 5 solved and 1 textbook result.

## `Transcendental.exp_add_pi_transcendental`

Open: stated without proof.

> $e + \pi$ is transcendental.

```lean
theorem exp_add_pi_transcendental : Transcendental ℚ (exp 1 + π)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 36](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L36).

## `Transcendental.exp_mul_pi_transcendental`

Open: stated without proof.

> $e\pi$ is transcendental.

```lean
theorem exp_mul_pi_transcendental : Transcendental ℚ (exp 1 * π)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L43).

## `Transcendental.exp_pow_pi_sq_transcendental`

Open: stated without proof.

> $e^{\pi^2}$ is transcendental.

```lean
theorem exp_pow_pi_sq_transcendental : Transcendental ℚ (exp (π ^ 2))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L50).

## `Transcendental.exp_exp_transcendental`

Open: stated without proof.

> $e^e$ is transcendental.

```lean
theorem exp_exp_transcendental : Transcendental ℚ (exp (exp 1))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L57).

## `Transcendental.pi_pow_exp_transcendental`

Open: stated without proof.

> $\pi^e$ is transcendental.

```lean
theorem pi_pow_exp_transcendental : Transcendental ℚ (π ^ (exp 1))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L64).

## `Transcendental.pi_pow_sqrt_two_transcendental`

Open: stated without proof.

> $\pi^{\sqrt{2}}$ is transcendental.

```lean
theorem pi_pow_sqrt_two_transcendental : Transcendental ℚ (π ^ √2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L71).

## `Transcendental.pi_pow_pi_transcendental`

Open: stated without proof.

> $\pi^{\pi}$ is transcendental.

```lean
theorem pi_pow_pi_transcendental : Transcendental ℚ (π ^ π)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L78).

## `Transcendental.pi_pow_pi_pow_pi_transcendental`

Open: stated without proof.

> $\pi^{\pi^{\pi}}$ is transcendental.

```lean
theorem pi_pow_pi_pow_pi_transcendental : Transcendental ℚ (π ^ (π ^ π))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L85).

## `Transcendental.pi_pow_pi_pow_pi_pow_pi_transcendental`

Open: stated without proof.

> $\pi^{\pi^{\pi^\pi}}$ is transcendental.

```lean
theorem pi_pow_pi_pow_pi_pow_pi_transcendental : Transcendental ℚ (π ^ (π ^ (π ^ π)))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L92).

## `Transcendental.pi_pow_pi_pow_pi_pow_pi_not_integer`

Open: stated without proof.

> $\pi^{\pi^{\pi^\pi}}$ is not an integer.
>
> This would follow from $\pi^{\pi^{\pi^\pi}}$ being transcendental,
> but this formulation is of interest in its own right,
> as it could in principle be proven by direct computation.
>
> *Reference:* [YouTube](https://www.youtube.com/watch?v=BdHFLfv-ThQ)

```lean
theorem pi_pow_pi_pow_pi_pow_pi_not_integer : ¬ ∃ (n : ℤ), π ^ π ^ π ^ π = n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L105).

## `Transcendental.rlog_pi_transcendental`

Open: stated without proof.

> $\log(\pi)$ is transcendental.

```lean
theorem rlog_pi_transcendental : Transcendental ℚ (log π)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L112).

## `Transcendental.rlog_rlog_two_transcendental`

Open: stated without proof.

> $\log(\log(2))$ is transcendental.

```lean
theorem rlog_rlog_two_transcendental : Transcendental ℚ ((2 : ℝ).log.log)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L119).

## `Transcendental.sin_exp_transcendental`

Open: stated without proof.

> $\sin(e)$ is transcendental.

```lean
theorem sin_exp_transcendental : Transcendental ℚ (Real.sin (exp 1))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 126](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L126).

## `Transcendental.exp_add_pi_or_exp_add_mul_transcendental`

Textbook result, stated without proof. A Lean proof is at [https://github.com/Aegis-Omega/AEGIS-OMEGA/blob/6703489001e7374c5fd963dc5f8e98c34ea567cb/research/formal-conjectures-pilot/ExpTranscendence.lean#L149-L153](https://github.com/Aegis-Omega/AEGIS-OMEGA/blob/6703489001e7374c5fd963dc5f8e98c34ea567cb/research/formal-conjectures-pilot/ExpTranscendence.lean#L149-L153).

> At least one of $\pi + e$ and $\pi e$ is transcendental.

```lean
theorem exp_add_pi_or_exp_add_mul_transcendental :
    Transcendental ℚ (π + rexp 1) ∨ Transcendental ℚ (π * exp 1)
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 135](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L135).

## `Transcendental.transcendental_eulerMascheroniConstant_or_gompertzConstant`

Solved: stated here without proof.

> At least one of the Euler–Mascheroni constant $\gamma$ and the Gompertz constant $\delta$ is
> transcendental.
>
> [Ri12] Rivoal, T. (2012). On the arithmetic nature of the values of the gamma function, Euler's
> constant, and Gompertz's constant. Michigan Mathematical Journal, 61(2), 239–254.

```lean
theorem transcendental_eulerMascheroniConstant_or_gompertzConstant :
    Transcendental ℚ eulerMascheroniConstant ∨ Transcendental ℚ gompertzConstant
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 147](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L147).

## `Transcendental.transcendental_catalanConstant`

Open: stated without proof.

> The Catalan constant $G$ is transcendental.

```lean
theorem transcendental_catalanConstant : Transcendental ℚ catalanConstant
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 155](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L155).

## `Transcendental.transcendental_gompertzConstant`

Open: stated without proof.

> The Gompertz constant $\delta$ is transcendental.

```lean
theorem transcendental_gompertzConstant : Transcendental ℚ gompertzConstant
```

Category `research open`; AMS [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 162](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L162).

## `Transcendental.transcendental_gamma_one_div_two`

Solved: stated here without proof.

> $\Gamma(1/2)$ is transcendental.
>
> [Ch84] Chudnovsky, G. (1984). Contributions to the theory of transcendental numbers.

```lean
theorem transcendental_gamma_one_div_two : Transcendental ℚ (1 / 2 : ℝ).Gamma
```

Category `research solved`; AMS [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 171](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L171).

## `Transcendental.transcendental_gamma_one_div_three`

Solved: stated here without proof.

> $\Gamma(1/3)$ is transcendental.
>
> [Ch84] Chudnovsky, G. (1984). Contributions to the theory of transcendental numbers.

```lean
theorem transcendental_gamma_one_div_three : Transcendental ℚ (1 / 3 : ℝ).Gamma
```

Category `research solved`; AMS [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 180](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L180).

## `Transcendental.transcendental_gamma_one_div_four`

Solved: stated here without proof.

> $\Gamma(1/4)$ is transcendental.
>
> [Ch84] Chudnovsky, G. (1984). Contributions to the theory of transcendental numbers.

```lean
theorem transcendental_gamma_one_div_four : Transcendental ℚ (1 / 4 : ℝ).Gamma
```

Category `research solved`; AMS [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 189](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L189).

## `Transcendental.transcendental_gamma_one_div_six`

Solved: stated here without proof.

> $\Gamma(1/6)$ is transcendental.
>
> [Ch84] Chudnovsky, G. (1984). Contributions to the theory of transcendental numbers.

```lean
theorem transcendental_gamma_one_div_six : Transcendental ℚ (1 / 6 : ℝ).Gamma
```

Category `research solved`; AMS [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 198](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L198).

## `Transcendental.transcendental_gamma_one_div`

Open: stated without proof.

> $\Gamma(1/n)$ for `n ≥ 2` is transcendental.

```lean
theorem transcendental_gamma_one_div (n : ℕ) (hn : 2 ≤ n) : Transcendental ℚ (1 / n : ℝ).Gamma
```

Category `research open`; AMS [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Transcendental.lean, line 205](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean#L205).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Transcendental.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Transcendental.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Transcendental_number)
