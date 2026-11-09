---
declaration: theorem
origin: cited
lean: Erdos1113.erdos_1113.variants.infinitely_many_sierpinski, Erdos1113.erdos_1113, Erdos1113.erdos_1113.variants.filaseta_finch_kozek
statement: formalized
---

# Erdős Problem 1113

> *References:*
> - [erdosproblems.com/1113](https://www.erdosproblems.com/1113)
> - [ErGr80] Erdős, P. and Graham, R. L., Old and New Problems and Results in Combinatorial
>   Number Theory. Monographie de l'Enseignement Mathématique, No. 28 (1980).
> - [Si60] Sierpiński, W., Elementary Theory of Numbers. Państwowe Wydawnictwo Naukowe,
>   Warsaw (1960).
> - [FFK08] Filaseta, M., Finch, C., and Kozek, M., On powers associated with Sierpiński numbers,
>   Riesel numbers and Polignac's conjecture. Journal of Number Theory 128 (2008), 1916–1940.
>
> A positive odd integer $k$ is a *Sierpiński number* if $k \cdot 2^n + 1$ is composite for all
> $n \geq 0$. A *covering set* for $k$ is a finite set of primes $P$ such that every number of
> the form $k \cdot 2^n + 1$ is divisible by at least one prime in $P$.
>
> Sierpiński (1960) proved that infinitely many Sierpiński numbers exist using covering systems.
> The smallest known Sierpiński number is 78557 (Selfridge). Erdős and Graham conjectured that
> there exist Sierpiński numbers with no finite covering set. A negative answer would imply
> infinitely many Fermat primes.
>
> Note: The notion of a covering set for a Sierpiński number is closely related to a
> `CoveringSystem` of $\mathbb{Z}$ (see
> `FormalConjecturesForMathlib.NumberTheory.CoveringSystem`): a finite covering set of primes
> for $k$ works because the exponents $n$ for which each prime divides $k \cdot 2^n + 1$ form
> residue classes whose union covers all of $\mathbb{Z}$, i.e. a covering system.
>
> See also Erdős Problems [203](https://www.erdosproblems.com/203) and
> [276](https://www.erdosproblems.com/276).

*Quoted from [FormalConjectures/ErdosProblems/1113.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1113.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1113](https://www.erdosproblems.com/1113).

The file states 3 research or textbook statements: 2 open and 1 solved.

## `Erdos1113.erdos_1113.variants.infinitely_many_sierpinski`

Solved: stated here; a Lean proof is at [https://github.com/HowieHwong/lean-erdos-proofs/blob/b8b641ba2d00dc4d1fe205a078a4159372672459/Erdos/P1113.lean#L22](https://github.com/HowieHwong/lean-erdos-proofs/blob/b8b641ba2d00dc4d1fe205a078a4159372672459/Erdos/P1113.lean#L22).

> Sierpiński [Si60] proved that there are infinitely many Sierpiński numbers, using covering
> systems to construct suitable covering sets for any $k$ satisfying a certain congruence.

```lean
theorem erdos_1113.variants.infinitely_many_sierpinski :
    Set.Infinite {k : ℕ | k.IsSierpinskiNumber}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1113.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1113.lean#L69).

## `Erdos1113.erdos_1113`

Open: stated without proof.

> **Erdős Problem 1113.** Do there exist Sierpiński numbers that possess no finite covering set
> of primes?
>
> Erdős and Graham [ErGr80] conjectured that the answer is yes. A negative answer would imply
> that there are infinitely many Fermat primes.

```lean
theorem erdos_1113 :
    ∃ k, k.IsSierpinskiNumber ∧ ¬ HasFinitePrimeCoveringSet k
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1113.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1113.lean#L81).

## `Erdos1113.erdos_1113.variants.filaseta_finch_kozek`

Open: stated without proof.

> **Filaseta–Finch–Kozek conjecture (2008).** Every Sierpiński number is either a perfect power
> or possesses a finite covering set of primes.

```lean
theorem erdos_1113.variants.filaseta_finch_kozek :
    ∀ k, k.IsSierpinskiNumber →
      k.IsPerfectPower ∨ HasFinitePrimeCoveringSet k
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1113.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1113.lean#L90).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1113.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1113.lean)
- [erdosproblems.com/1113](https://www.erdosproblems.com/1113)
