---
declaration: theorem
origin: cited
lean: Erdos717.erdos_717, Erdos717.erdos_717.variants.erdos_fajtlowicz
statement: formalized
---

# Erdős Problem 717

> *References:*
> - [erdosproblems.com/717](https://www.erdosproblems.com/717)
> - [ErFa81] Erdős, Paul and Fajtlowicz, Siemion, *On the conjecture of Hajós*. Combinatorica 1
>   (1981), 141-143. [PDF](https://www.renyi.hu/~p_erdos/1981-17.pdf)
> - [FLS13] Fox, Jacob and Lee, Choongbum and Sudakov, Benny, *Chromatic number, clique
>   subdivisions, and the conjectures of Hajós and Erdős-Fajtlowicz*. Combinatorica 33 (2013),
>   181-197. [arXiv:1107.1920](https://arxiv.org/abs/1107.1920)

*Quoted from [FormalConjectures/ErdosProblems/717.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/717.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/717](https://www.erdosproblems.com/717).

The file states 2 research or textbook statements: 2 solved. It also has 2 test statements and 3 API statements, counted here but not shown.

## `Erdos717.erdos_717`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos717.lean#L573](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos717.lean#L573).

> Let $G$ be a graph on $n$ vertices with chromatic number $\chi(G)$ and let $\sigma(G)$ be the
> maximal $k$ such that $G$ contains a subdivision of $K_k$. Is it true that
> $$\chi(G) \ll \frac{n^{1/2}}{\log n}\sigma(G)?$$
>
> The answer is yes, proved by Fox, Lee, and Sudakov [FLS13, Theorem 1.1]. We read $\ll$ as: there
> is an absolute constant $C > 0$ with this inequality for all graphs on $n \geq 2$ vertices
> (for $n = 1$, $\log n = 0$).

```lean
theorem erdos_717 :
    ∃ C : ℝ, 0 < C ∧
      ∀ (V : Type) [Fintype V] (G : SimpleGraph V),
        2 ≤ Fintype.card V →
        (G.chromaticNumber.toNat : ℝ) ≤
          C * (Real.sqrt (Fintype.card V : ℝ) / Real.log (Fintype.card V : ℝ)) *
            (cliqueSubdivisionNumber G : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/717.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/717.lean#L121).

## `Erdos717.erdos_717.variants.erdos_fajtlowicz`

Solved: stated here without proof.

> Erdős and Fajtlowicz [ErFa81, Theorem 3] showed that for almost all graphs on $n$ vertices
> $$\chi(G) \gg \frac{n^{1/2}}{\log n}\sigma(G).$$
> As in [ErFa81, p. 141], "almost all" means all but $o(2^{\binom{n}{2}})$ labelled graphs on $n$
> vertices.

```lean
theorem erdos_717.variants.erdos_fajtlowicz :
    ∃ C : ℝ, 0 < C ∧
      Tendsto (fun n : ℕ =>
        (Nat.card {G : SimpleGraph (Fin n) //
          ¬ (C * (Real.sqrt n / Real.log n) * (cliqueSubdivisionNumber G : ℝ) <
            (G.chromaticNumber.toNat : ℝ))} : ℝ) / 2 ^ n.choose 2) atTop (𝓝 0)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/717.lean, line 137](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/717.lean#L137).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/717.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/717.lean)
- [erdosproblems.com/717](https://www.erdosproblems.com/717)
