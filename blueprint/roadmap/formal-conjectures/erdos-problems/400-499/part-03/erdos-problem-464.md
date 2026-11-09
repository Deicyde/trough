---
declaration: theorem
origin: cited
lean: Erdos464.erdos_464
statement: formalized
---

# Erdős Problem 464

> *References:*
> - [erdosproblems.com/464](https://www.erdosproblems.com/464)
> - [Er75i] Erdős, P., *Répartition modulo $1$*. (1975), iv+258.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial
>   number theory*. Monographies de L'Enseignement Mathématique (1980).
> - [Er82e] Erdős, Paul, *Some of my favourite problems which recently have been solved*.
>   (1982), 59--79.
> - [AkMo04] Akhunzhanov, R. K. and Moshchevitin, N. G., *On the chromatic number of a distance
>   graph associated with a lacunary sequence*. Dokl. Akad. Nauk (2004), 295-296.
> - [Du06] Dubickas, Artūras, *On the fractional parts of lacunary sequences*. Math. Scand. (2006),
>   136-146.
> - [Ka01] Katznelson, Y., *Chromatic numbers of Cayley graphs on $\mathbb{Z}$ and recurrence*.
>   Combinatorica (2001), 211-219.
> - [PeSc10] Peres, Yuval and Schlag, Wilhelm, *Two Erdős problems on lacunary sequences: chromatic
>   number and Diophantine approximation*. Bull. Lond. Math. Soc. (2010), 295-300.
> - [Po79b] Pollington, A. D., *On the density of sequence $\{n_k\xi\}$*. Illinois J. Math. (1979),
>   511-515.
> - [dM80] de Mathan, B., *Numbers contravening a condition in density modulo $1$*. Acta Math.
>   Acad. Sci. Hungar. (1980), 237-241 (1981).

*Quoted from [FormalConjectures/ErdosProblems/464.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/464.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/464](https://www.erdosproblems.com/464).

The file states 1 research or textbook statement: 1 solved.

## `Erdos464.erdos_464`

Solved: stated here; a Lean proof is at [https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/464/Erdos464.lean](https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/464/Erdos464.lean).

> Let $A=\{n_1\lt n_2\lt \cdots\}\subset \mathbb{N}$ be a lacunary sequence (so there exists some
> $\epsilon>0$ with $n_{k+1}\geq (1+\epsilon)n_k$ for all $k$). Must there exist an irrational
> $\theta$ such that
>
> $$\{ \|\theta n_k\| : k\geq 1\}$$
>
> is not dense in $[0,1]$ (where $\| x\|$ is the distance to the nearest integer)?
>
> Solved independently by de Mathan [dM80] and Pollington [Po79b], who showed that, given any
> such $A$, there exists such a $\theta$, with
>
> $$\inf_{k\geq 1}\| \theta n_k\| \gg \frac{\epsilon^4}{\log(1/\epsilon)}.$$
>
> This bound was improved by Katznelson [Ka01], Akhunzhanov and Moshchevitin [AkMo04], and
> Dubickas [Du06], before Peres and Schlag [PeSc10] improved it to
>
> $$\inf_{k\geq 1}\| \theta n_k\| \gg \frac{\epsilon}{\log(1/\epsilon)},$$
>
> and note that the best bound possible here would be $\gg \epsilon$.
>
> This problem has consequences for [894](https://www.erdosproblems.com/894).
>
> The conclusion "$\{\|\theta n_k\|\}$ is not dense in $[0,1]$" is formalized as the sequence
> $(\theta n_k)$ not being dense modulo one; see the formalization notes above.

```lean
theorem erdos_464 :
    ∀ n : ℕ → ℕ, StrictMono n → (∀ k, 0 < n k) → IsLacunary n →
      ∃ θ : ℝ, Irrational θ ∧
        ¬ Dense (Set.range fun k => (↑(θ * n k) : AddCircle (1 : ℝ)))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/464.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/464.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/464.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/464.lean)
- [erdosproblems.com/464](https://www.erdosproblems.com/464)
