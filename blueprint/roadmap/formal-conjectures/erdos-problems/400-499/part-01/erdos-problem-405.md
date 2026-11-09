---
declaration: theorem
origin: cited
lean: Erdos405.erdos_405, Erdos405.erdos_405.variants.nonodd_p, Erdos405.erdos_405.variants.yu_liu
statement: formalized
---

# Erdős Problem 405

> *References:*
> - [erdosproblems.com/405](https://www.erdosproblems.com/405)
> - [ErGr80] Erdős, P. and Graham, R., Old and new problems and results in combinatorial number
> theory. Monographies de L'Enseignement Mathematique (1980)
> - [BrEr91] Brindza, B. and Erdős, P., On some {D}iophantine problems involving powers and
> factorials. J. Austral. Math. Soc. Ser. A (1991), 1--7.
> - [YuLi96] Yu, Kunrui and Liu, Dehua, A complete resolution of a problem of {E}rdős and {G}raham.
> Rocky Mountain J. Math. (1996), 1235--1244.

*Quoted from [FormalConjectures/ErdosProblems/405.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/405.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/405](https://www.erdosproblems.com/405).

The file states 3 research or textbook statements: 2 solved and 1 textbook result.

## `Erdos405.erdos_405`

Solved: stated here without proof.

> Let $p$ be an odd prime. Is it true that the equation $(p-1)!+a^{p-1}=p^k$ has only finitely many
> solutions?
>
> Originally proposed by Erdős and Graham [ErGr80].
> Brindza and Erdős [BrEr91] proved that there are finitely many such solutions.

```lean
theorem erdos_405 :
    Set.Finite { x : ℕ × ℕ × ℕ | let (a, k, p) := x; p.Prime ∧ Odd p ∧
      Nat.factorial (p - 1) + a ^ (p - 1) = p ^ k}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/405.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/405.lean#L48).

## `Erdos405.erdos_405.variants.nonodd_p`

Textbook result, proved here.

> Erdős and Graham [ErGr80] ask this allowing $p=2$, but this is presumably an oversight, since clearly
> there are infinitely many solutions when $p=2$.
>
> Observe that this creates $1! + a = 2^k$. For all $k$, fix $a = 2^k - 1$.

```lean
theorem erdos_405.variants.nonodd_p :
    Set.Infinite { x : ℕ × ℕ × ℕ | let (a, k, p) := x; p.Prime ∧
      Nat.factorial (p - 1) + a ^ (p - 1) = p ^ k}
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/405.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/405.lean#L60).

## `Erdos405.erdos_405.variants.yu_liu`

Solved: stated here without proof.

> Yu and Liu [YuLi96] showed that the only solutions to $(p-1)! + a^(p-1) = p^k$
> for an odd prime p are:
> $$
> 2! + 1^2 = 3\\
> 2! + 5^2 = 3^3\\
> 4! + 1^4 = 5^2
> $$

```lean
theorem erdos_405.variants.yu_liu :
    { x : ℕ × ℕ × ℕ | let (a, k, p) := x; p.Prime ∧ Odd p ∧
      Nat.factorial (p - 1) + a ^ (p - 1) = p ^ k } =
    {(1, 1, 3), (5, 3, 3), (1, 2, 5)}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/405.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/405.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/405.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/405.lean)
- [erdosproblems.com/405](https://www.erdosproblems.com/405)
