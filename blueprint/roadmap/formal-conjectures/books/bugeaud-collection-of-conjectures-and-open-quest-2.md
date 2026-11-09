---
declaration: theorem
origin: cited
lean: Bugeaud04.spectrum_xi_alpha_pow_countable
statement: formalized
---

# Bugeaud Collection of Conjectures and Open Questions: Spectrum of Sequence

> *References:*
>   - [Bug12] Bugeaud, Yann. "Distribution modulo one and Diophantine approximation."
>     Vol. 193. Cambridge University Press, 2012. Chapter 10.
>   - [Men73] Mendès France, Michel. "Les ensembles de Bésineau."
>     Séminaire Delange-Pisot-Poitou 15.1 (1973): 1-6.
>   - [Özc26] Özcan, Hikmet Burak. "The spectrum of $(\xi\alpha^n)$ can be uncountable."
>     [arXiv:2609.07714](https://arxiv.org/abs/2609.07714) (2026).
>
> ## Counterexample
>
> Problem 10.4 is false. Özcan [Özc26] proves that for every real $\alpha > 1$ there are
> $2^{\aleph_0}$ reals $\xi > 0$ whose spectrum contains one and the same uncountable set.
> The counterexample below is an independent, self-contained instance of this for the base
> $\alpha = 64$, where the digits of $\xi$ can be prescribed directly.
>
> For a bit sequence $u \in \{0, 1\}^{\mathbb{N}}$ put
> $$\theta_u = \sum_{i \ge 0} (1 + u_i) \, 8^{-e(i)}, \qquad e(i) = 4^{i+1} + i + 6.$$
> The map $u \mapsto \theta_u$ is injective with values in $(0, 1)$.
>
> Split the indices into the blocks $[5 m_k, 6 m_k)$ with $m_k = 20 \cdot 8^k$; these are
> pairwise disjoint. Block number $k = \langle L, c \rangle$, where $\langle \cdot, \cdot \rangle$
> is the Cantor pairing, is reserved for the bit string $c$ of length $L$. On that block the
> base-$64$ digits of $\xi$ are chosen so that $\{\xi 64^n\}$ shadows $\{n \theta\}$ for every
> $\theta$ whose first $L$ bits are $c$. This is possible because one base-$64$ digit pins down
> $\{\xi 64^n\}$ up to $2/64$, and because $k \le 4^{L+1}$ forces the block to sit far to the left
> of the precision $8^{-e(L)}$ of the truncation of $\theta$, so that $n$ times the truncation
> error stays below $1/512$ on the block.
>
> Consequently $\{\xi 64^n - n \theta_u\} < 1/10$ for all $n$ in the block attached to the first
> $L$ bits of $u$, for every $L$. That block is the last sixth of $[0, 6 m_k)$, so at the times
> $N = 6 m_k - 6$ at most a proportion $5/6$ of the points $\{\xi 64^n - n\theta_u\}$ with $n < N$
> lies in $[1/10, 1]$, whereas uniform distribution modulo one would force the proportion
> $9/10$. Hence every irrational $\theta_u$ lies in the spectrum of $(\xi 64^n)$, and since
> $\{\theta_u\}$ is uncountable the spectrum cannot be countable.

*Quoted from [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_4.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_4.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `Bugeaud04.spectrum_xi_alpha_pow_countable`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/8e2413a849b19822431772684d41cdc31637a409/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_4.lean#L682](https://github.com/mo271/formal-conjectures/blob/8e2413a849b19822431772684d41cdc31637a409/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_4.lean#L682).

> Problem 10.4. Let $\xi$ be a non-zero real number and $\alpha > 1$ be a real
> number. Is the spectrum of the sequence $(\xi \alpha^n)_{n \ge 1}$ at most
> countable? Posed by Mendès France [Men73].
>
> The answer is no. Özcan [Özc26] disproved this for every $\alpha > 1$; the counterexample
> formalised here takes $\alpha = 64$ and the real number $\xi = $ `xiVal`, whose spectrum
> contains the uncountable set of irrational numbers of the form `thetaSeq u`.

```lean
theorem spectrum_xi_alpha_pow_countable :
    ¬ ∀ (ξ : ℝ), ξ ≠ 0 → ∀ (α : ℝ), 1 < α → (Spectrum (fun n => ξ * α ^ n)).Countable
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_4.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_4.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_4.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_4.lean)
- [arXiv:2609.07714](https://arxiv.org/abs/2609.07714)
