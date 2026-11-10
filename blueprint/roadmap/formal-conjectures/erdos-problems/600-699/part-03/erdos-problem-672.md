---
declaration: theorem
origin: cited
lean: Erdos672.erdos_672, Erdos672.erdos_672.variants.euler, Erdos672.erdos_672.variants.oblath
statement: formalized
---

# Erdős Problem 672

> *Reference:* [erdosproblems.com/672](https://www.erdosproblems.com/672)

*Quoted from [FormalConjectures/ErdosProblems/672.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/672.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/672](https://www.erdosproblems.com/672).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos672.erdos_672`

Open: stated without proof.

> Can the product of an arithmetic progression of positive integers $n, n + d, ..., n + (k - 1)d$
> of length $k ≥ 4$, with $(n, d) = 1$, be a perfect power?
>
> Erdős believed not, i.e. that `Erdos672With k l` holds for all $k ≥ 4$ and $l > 1$.

```lean
theorem erdos_672 :
    ∃ᵉ (k ≥ 4) (l > 1), ¬ Erdos672With k l
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/672.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/672.lean#L42).

## `Erdos672.erdos_672.variants.euler`

Solved: stated here; a Lean proof is at [https://github.com/herakles-dev/erdos672-four-squares-lean/blob/68adec55180c6103ac5511a5c91c84b25a5044f9/Erdos672/Statement.lean#L41](https://github.com/herakles-dev/erdos672-four-squares-lean/blob/68adec55180c6103ac5511a5c91c84b25a5044f9/Erdos672/Statement.lean#L41).

> According to https://www.erdosproblems.com/672, Euler proved this.

```lean
lemma erdos_672.variants.euler :
    Erdos672With 4 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/672.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/672.lean#L49).

## `Erdos672.erdos_672.variants.oblath`

Solved: stated here without proof.

> According to https://www.erdosproblems.com/672, Obláth proved this.
>
> [Ob51] Oblath, Richard, Eine Bemerkung über Produkte aufeinander folgender Zahlen.
> J. Indian Math. Soc. (N.S.) (1951), 135-139.

```lean
lemma erdos_672.variants.oblath :
    Erdos672With 5 2 ∧ Erdos672With 3 3 ∧ Erdos672With 3 4 ∧ Erdos672With 3 5
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/672.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/672.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/672.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/672.lean)
- [erdosproblems.com/672](https://www.erdosproblems.com/672)
