---
declaration: theorem
origin: cited
lean: Erdos897.erdos_897.parts.i, Erdos897.erdos_897.parts.ii, Erdos897.erdos_897.variants.log_growth, Erdos897.erdos_897.variants.parts.i, Erdos897.erdos_897.variants.parts.ii
statement: formalized
---

# Erdős Problem 897

> *References:*
> - [erdosproblems.com/897](https://www.erdosproblems.com/897)
> - [Ar25] Archivara Math Research Agent, [An Additive Counterexample: Erdős Problem 897](https://archivara.org/paper/df04f023-6ef0-4c52-bd12-18cdaa8f0741) (2025)
> - [ArWu25] Aristotle, operated mostly by L. Wu, [Lean formalisation of Erdős problem 897](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos897.lean) (2025)
> - [Wi70] E. Wirsing, A characterization of $\log n$ as an additive arithmetic function.
>   Symposia Math. (1970), 45-57.
> - [Wi81] E. Wirsing, Additive and completely additive functions with restricted growth.
>   Recent progress in analytic number theory, Vol. 2 (Durham, 1979), 231--280 (1981).

*Quoted from [FormalConjectures/ErdosProblems/897.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/897.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/897](https://www.erdosproblems.com/897).

The file states 5 research or textbook statements: 2 open and 3 solved.

## `Erdos897.erdos_897.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos897.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos897.lean).

> Let $f(n)$ be an additive function (so that $f(ab)=f(a)+f(b)$
> if $(a,b)=1$ such that $\limsup_{p,k} f(p^k) / \log(p^k) = ∞$.
> Is it true that $\limsup_n (f(n+1)−f(n))/ \log n = ∞$?
>
> The answer is no; this follows from a construction of Wirsing [Wi81], rediscovered by
> Archivara [Ar25] and formalised in Lean by Aristotle [ArWu25].

```lean
theorem erdos_897.parts.i : ¬ ∀ (f : ℕ → ℝ),
    (∀ᵉ (a > 0) (b > 0), a.Coprime b → f (a * b) = f a + f b) →
    ((Filter.atTop ⊓ Filter.principal {(p, k) : ℕ × ℕ | p.Prime}).limsup
      (fun (p, k) => (f (p^k) / (p^k : ℝ).log : EReal)) = ⊤) →
    Filter.atTop.limsup (fun (n : ℕ) => ((f (n+1) - f n) / (n : ℝ).log : EReal)) = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/897.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/897.lean#L49).

## `Erdos897.erdos_897.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos897.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos897.lean).

> Let $f(n)$ be an additive function (so that $f(ab)=f(a)+f(b)$
> if $(a,b)=1$) such that $\limsup_{p,k} f(p^k) / \log(p^k) = ∞$.
> Is it true that $\limsup_n f(n+1)/ f(n) = ∞$?
>
> The answer is no; the same counterexample is formalised in Lean by Aristotle [ArWu25].

```lean
theorem erdos_897.parts.ii : ¬ ∀ (f : ℕ → ℝ),
    (∀ᵉ (a > 0) (b > 0), a.Coprime b → f (a * b) = f a + f b) →
    ((Filter.atTop ⊓ Filter.principal {(p, k) : ℕ × ℕ | p.Prime}).limsup
      (fun (p, k) => (f (p^k) / (p^k : ℝ).log : EReal)) = ⊤) →
    Filter.atTop.limsup (fun (n : ℕ) => (f (n+1) / f n : EReal)) = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/897.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/897.lean#L66).

## `Erdos897.erdos_897.variants.log_growth`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos491.lean#L34](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos491.lean#L34).

> Wirsing [Wi70] proved that if $|f(n+1)−f(n)| ≤ C$ then $f(n) = c \log n + O(1)$ for some constant
> $c$. This is Erdős Problem 491; see `erdos_491`, whose linked formal proof gives this statement.

```lean
theorem erdos_897.variants.log_growth
    (f : ℕ → ℝ)
    (hf : ∀ᵉ (a > 0) (b > 0), a.Coprime b → f (a * b) = f a + f b)
    (C : ℝ) (hf' : ∀ n, |f (n+1) - f n| ≤ C) :
    ∃ c, ∃ (O : ℕ → ℝ), O =O[Filter.atTop] (1 : ℕ → ℝ) ∧
      ∀ n, f n ≤ c*Real.log n + O n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/897.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/897.lean#L80).

## `Erdos897.erdos_897.variants.parts.i`

Open: stated without proof.

> Let $f(n)$ be an additive function (so that $f(ab)=f(a)+f(b)$
> if $(a,b)=1$) such that $\limsup_{p,k} f(p^k) / \log(p^k) = ∞$ and $f(p^k) = f(p)$
> or $f(p^k) = kf(p)$.
> Is it true that $\limsup_n (f(n+1)−f(n))/ \log n = ∞$?
>
> The known counterexample does not satisfy either of these extra hypotheses, so this variant remains
> open.

```lean
theorem erdos_897.variants.parts.i : ∀ (f : ℕ → ℝ),
    (∀ᵉ (a > 0) (b > 0), a.Coprime b → f (a * b) = f a + f b) →
    ((Filter.atTop ⊓ Filter.principal {(p, k) : ℕ × ℕ | p.Prime}).limsup
      (fun (p, k) => (f (p^k) / (p^k : ℝ).log : EReal)) = ⊤) →
    (∀ k p, p.Prime → f (p^k) = f p) ∨ (∀ (k p : ℕ), p.Prime → f (p^k) = k*f p) →
    Filter.atTop.limsup (fun (n : ℕ) => ((f (n+1) - f n) / (n : ℝ).log : EReal)) = ⊤
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/897.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/897.lean#L99).

## `Erdos897.erdos_897.variants.parts.ii`

Open: stated without proof.

> Let $f(n)$ be an additive function (so that $f(ab)=f(a)+f(b)$
> if $(a,b)=1$) such that $\limsup_{p,k} f(p^k) / \log(p^k) = ∞$ and $f(p^k) = f(p)$
> or $f(p^k) = kf(p)$.
> Is it true that $\limsup_n f(n+1)/f(n) = ∞$?
>
> The known counterexample does not satisfy either of these extra hypotheses, so this variant remains
> open.

```lean
theorem erdos_897.variants.parts.ii : ∀ (f : ℕ → ℝ),
    (∀ᵉ (a > 0) (b > 0), a.Coprime b → f (a * b) = f a + f b) →
    ((Filter.atTop ⊓ Filter.principal {(p, k) : ℕ × ℕ | p.Prime}).limsup
      (fun (p, k) => (f (p^k) / (p^k : ℝ).log : EReal)) = ⊤) →
    (∀ k p, p.Prime → f (p^k) = f p) ∨ (∀ (k p : ℕ), p.Prime → f (p^k) = k*f p) →
    Filter.atTop.limsup (fun (n : ℕ) => (f (n+1) / f n : EReal)) = ⊤
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/897.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/897.lean#L117).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/897.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/897.lean)
- [erdosproblems.com/897](https://www.erdosproblems.com/897)
