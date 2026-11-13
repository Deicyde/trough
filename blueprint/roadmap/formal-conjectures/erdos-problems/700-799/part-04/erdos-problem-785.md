---
declaration: theorem
origin: cited
lean: Erdos785.erdos_785, Erdos785.erdos_785.variants.danzer, Erdos785.erdos_785.variants.sarkozy_szemeredi, Erdos785.erdos_785.variants.chen_fang, Erdos785.erdos_785.variants.narkiewicz, Erdos785.erdos_785.variants.ruzsa_upper_bound, Erdos785.erdos_785.variants.ruzsa_lower_bound, Erdos785.erdos_785.variants.chen_fang_limsup, Erdos785.erdos_785.variants.chen_conjecture, Erdos785.erdos_785.variants.chen_fang_sharp
statement: formalized
---

# Erdős Problem 785

> *References:*
> - [erdosproblems.com/785](https://www.erdosproblems.com/785)
> - [ChFa10] Fang, Jin-Hui and Chen, Yong-Gao, *On additive complements*. Proc. Amer. Math. Soc.
>   (2010), 1923-1927.
> - [ChFa11] Chen, Yong-Gao and Fang, Jin-Hui, *On additive complements. II*. Proc. Amer. Math. Soc.
>   (2011), 881-883.
> - [ChFa14] Fang, Jin-Hui and Chen, Yong-Gao, *On additive complements. III*. J. Number Theory
>   (2014), 83-91.
> - [ChFa15] Chen, Yong-Gao and Fang, Jin-Hui, *On a conjecture of Sárközy and Szemerédi*.
>   Acta Arith. (2015), 47-58.
> - [Da64] Danzer, L., *Über eine Frage von G. Hanani aus der additiven Zahlentheorie*.
>   J. Reine Angew. Math. (1964), 392-394.
> - [Er57] Erdős, Paul, *Some unsolved problems*. Michigan Math. J. (1957), 291-300.
> - [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
>   221-254.
> - [Na59] Narkiewicz, Władysław, *Remarks on a conjecture of Hanani in additive number theory*.
>   Colloq. Math. (1959/60), 161-165.
> - [Ru17] Ruzsa, Imre Z., *Exact additive complements*. Q. J. Math. (2017), 227-235.
> - [SaSz94] Sárközy, A. and Szemerédi, E., *On a problem in additive number theory*.
>   Acta Math. Hungar. (1994), 237-245.

*Quoted from [FormalConjectures/ErdosProblems/785.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/785.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/785](https://www.erdosproblems.com/785).

The file states 10 research or textbook statements: 1 open and 9 solved.

## `Erdos785.erdos_785`

Solved: stated here; a Lean proof is at [https://github.com/Woett/Lean-files/blob/main/ErdosProblem785.lean](https://github.com/Woett/Lean-files/blob/main/ErdosProblem785.lean).

> Let $A,B\subseteq \mathbb{N}$ be infinite sets of positive integers such that $A+B$ contains all
> large integers. Let $A(x)=\lvert A\cap [1,x]\rvert$ and similarly for $B(x)$. Is it true that if
> $A(x)B(x)\sim x$ then
>
> $$A(x)B(x)-x\to \infty$$
>
> as $x\to \infty$?
>
> A conjecture of Erdős and Danzer. The answer is yes, proved by Sárközy and Szemerédi [SaSz94],
> who actually proved that it is impossible for
>
> $$A(x)B(x)-x=o(A(x)).$$
>
> This was formalized in Lean by van Doorn using Aristotle.

```lean
theorem erdos_785 :
    ∀ A B : Set ℕ, A.Infinite → B.Infinite → 0 ∉ A → 0 ∉ B → IsExactAdditiveComplement A B →
      Tendsto (fun x : ℕ => (counting A x * counting B x : ℝ) - (x : ℝ)) atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/785.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/785.lean#L83).

## `Erdos785.erdos_785.variants.danzer`

Solved: stated here without proof.

> Danzer [Da64] proved that exact additive complements exist (Hanani had earlier conjectured they
> do not exist, as reported in [Er57] and [Er61]).

```lean
theorem erdos_785.variants.danzer :
    ∃ A B : Set ℕ, A.Infinite ∧ B.Infinite ∧ 0 ∉ A ∧ 0 ∉ B ∧ IsExactAdditiveComplement A B
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/785.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/785.lean#L93).

## `Erdos785.erdos_785.variants.sarkozy_szemeredi`

Solved: stated here without proof.

> Sárközy and Szemerédi [SaSz94] proved that it is impossible for
>
> $$A(x)B(x)-x=o(A(x)).$$

```lean
theorem erdos_785.variants.sarkozy_szemeredi (A B : Set ℕ) (hA : A.Infinite) (hB : B.Infinite)
    (hA₀ : 0 ∉ A) (hB₀ : 0 ∉ B) (h : IsExactAdditiveComplement A B) :
    ¬ (fun x : ℕ => (counting A x * counting B x : ℝ) - (x : ℝ)) =o[atTop]
      (fun x : ℕ => (counting A x : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/785.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/785.lean#L102).

## `Erdos785.erdos_785.variants.chen_fang`

Solved: stated here without proof.

> Chen and Fang [ChFa15] proved $A(x)B(x)-x\ll \min(A(x),B(x))^c$ cannot hold for any constant
> $c>0$. In particular $A(x)B(x)-x\ll A(x)^c$ cannot hold when $A$ is the sparser of the two sets.

```lean
theorem erdos_785.variants.chen_fang (A B : Set ℕ) (hA : A.Infinite) (hB : B.Infinite)
    (hA₀ : 0 ∉ A) (hB₀ : 0 ∉ B) (h : IsExactAdditiveComplement A B) (c : ℝ) (hc : 0 < c) :
    ¬ (fun x : ℕ => (counting A x * counting B x : ℝ) - (x : ℝ)) =O[atTop]
      (fun x : ℕ => (min (counting A x) (counting B x) : ℝ) ^ c)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/785.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/785.lean#L113).

## `Erdos785.erdos_785.variants.narkiewicz`

Solved: stated here without proof.

> Narkiewicz [Na59] proved that, under the given assumptions (and perhaps swapping $A$ and $B$)
> we must have $A(2x)/A(x)\to 1$ and $B(2x)/B(x)\to 2$.

```lean
theorem erdos_785.variants.narkiewicz (A B : Set ℕ) (hA : A.Infinite) (hB : B.Infinite)
    (hA₀ : 0 ∉ A) (hB₀ : 0 ∉ B) (h : IsExactAdditiveComplement A B) :
    (Tendsto (fun x : ℕ => (counting A (2 * x) : ℝ) / (counting A x : ℝ)) atTop (𝓝 1) ∧
      Tendsto (fun x : ℕ => (counting B (2 * x) : ℝ) / (counting B x : ℝ)) atTop (𝓝 2)) ∨
    (Tendsto (fun x : ℕ => (counting B (2 * x) : ℝ) / (counting B x : ℝ)) atTop (𝓝 1) ∧
      Tendsto (fun x : ℕ => (counting A (2 * x) : ℝ) / (counting A x : ℝ))
        atTop (𝓝 2))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/785.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/785.lean#L124).

## `Erdos785.erdos_785.variants.ruzsa_upper_bound`

Solved: stated here without proof.

> Ruzsa [Ru17] has constructed, for any function $w(x)\to \infty$, such a pair of sets with
>
> $$A(x)B(x)-x\lt w(x)$$
>
> for infinitely many $x$.

```lean
theorem erdos_785.variants.ruzsa_upper_bound (w : ℕ → ℝ) (hw : Tendsto w atTop atTop) :
    ∃ A B : Set ℕ, A.Infinite ∧ B.Infinite ∧ 0 ∉ A ∧ 0 ∉ B ∧ IsExactAdditiveComplement A B ∧
      ∃ᶠ x : ℕ in atTop, (counting A x * counting B x : ℝ) - (x : ℝ) < w x
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/785.lean, line 139](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/785.lean#L139).

## `Erdos785.erdos_785.variants.ruzsa_lower_bound`

Solved: stated here without proof.

> Ruzsa [Ru17] proves that, if $a^*(x)=\max A \cap [1,x]$ and $A$ and $B$ satisfy the conditions
> in the problem then (after possibly changing the roles of $A$ and $B$)
>
> $$A(x)B(x)-x > (1-o(1))\frac{a^*(x)}{A(x)}.$$

```lean
theorem erdos_785.variants.ruzsa_lower_bound (A B : Set ℕ) (hA : A.Infinite) (hB : B.Infinite)
    (hA₀ : 0 ∉ A) (hB₀ : 0 ∉ B) (h : IsExactAdditiveComplement A B) :
    (∀ ε > (0 : ℝ), ∀ᶠ x : ℕ in atTop,
        (1 - ε) * (aStar A x : ℝ) / (counting A x : ℝ)
          < (counting A x * counting B x : ℝ) - (x : ℝ)) ∨
    (∀ ε > (0 : ℝ), ∀ᶠ x : ℕ in atTop,
        (1 - ε) * (aStar B x : ℝ) / (counting B x : ℝ)
          < (counting A x * counting B x : ℝ) - (x : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/785.lean, line 150](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/785.lean#L150).

## `Erdos785.erdos_785.variants.chen_fang_limsup`

Solved: stated here without proof.

> Chen and Fang [ChFa10] proved the stronger statement that $A(x)B(x)-x\to \infty$ if $A$ and $B$
> are infinite sets such that $A+B$ contains all large integers and
>
> $$\limsup_{x\to \infty}\frac{A(x)B(x)}{x}\lt \frac{5}{4}.$$
>
> They later [ChFa14] improved $5/4$ to $3-\sqrt{3}\approx 1.268$.

```lean
theorem erdos_785.variants.chen_fang_limsup (A B : Set ℕ) (hA : A.Infinite) (hB : B.Infinite)
    (hA₀ : 0 ∉ A) (hB₀ : 0 ∉ B) (h : IsAdditiveComplement A B)
    (hlim : limsup (fun x : ℕ => ((counting A x * counting B x : ℝ) / (x : ℝ) : EReal)) atTop
      < ((3 - Real.sqrt 3 : ℝ) : EReal)) :
    Tendsto (fun x : ℕ => (counting A x * counting B x : ℝ) - (x : ℝ)) atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/785.lean, line 167](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/785.lean#L167).

## `Erdos785.erdos_785.variants.chen_conjecture`

Open: stated without proof.

> Chen conjectures that this should be true with $3/2$.

```lean
theorem erdos_785.variants.chen_conjecture :
    ∀ A B : Set ℕ, A.Infinite → B.Infinite → 0 ∉ A → 0 ∉ B → IsAdditiveComplement A B →
      limsup (fun x : ℕ => ((counting A x * counting B x : ℝ) / (x : ℝ) : EReal)) atTop
          < ((3 / 2 : ℝ) : EReal) →
        Tendsto (fun x : ℕ => (counting A x * counting B x : ℝ) - (x : ℝ)) atTop atTop
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/785.lean, line 178](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/785.lean#L178).

## `Erdos785.erdos_785.variants.chen_fang_sharp`

Solved: stated here without proof.

> This is sharp, as Chen and Fang [ChFa11] also proved that there exist such $A$ and $B$ with
>
> $$\limsup_{x\to \infty}\frac{A(x)B(x)}{x}=\frac{3}{2}$$
>
> for which $A(x)B(x)-x=1$ for infinitely many $x$.

```lean
theorem erdos_785.variants.chen_fang_sharp :
    ∃ A B : Set ℕ, A.Infinite ∧ B.Infinite ∧ 0 ∉ A ∧ 0 ∉ B ∧ IsAdditiveComplement A B ∧
      limsup (fun x : ℕ => ((counting A x * counting B x : ℝ) / (x : ℝ) : EReal)) atTop
          = ((3 / 2 : ℝ) : EReal) ∧
      ∃ᶠ x : ℕ in atTop, (counting A x * counting B x : ℝ) - (x : ℝ) = 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/785.lean, line 191](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/785.lean#L191).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/785.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/785.lean)
- [erdosproblems.com/785](https://www.erdosproblems.com/785)
