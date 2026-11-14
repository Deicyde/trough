---
declaration: lemma
origin: cited
lean: MIPRE.AnswerReduction.arVerifier_soundness, MIPRE.AnswerReduction.FieldLarge, MIPRE.AnswerReduction.errE, MIPRE.AnswerReduction.errE_le, MIPRE.AnswerReduction.sqrt_le_delta, MIPRE.AnswerReduction.exists_threshold_clB, MIPRE.AnswerReduction.z_le, MIPRE.AnswerReduction.soundA, MIPRE.AnswerReduction.soundC, MIPRE.AnswerReduction.one_le_delta_of_trivial, MIPRE.AnswerReduction.val_ge_of_arStrategy, MIPRE.AnswerReduction.arVerifier_soundness_tensor
statement: formalized
proof: formalized
---

# Answer-reduction quantitative assembly

Put $L=(\lambda n)^\mu$, $\rho=m'd/q$ and $E=\delta_{\mathrm{CL}}(\theta,q,m',d,m'+6)$ for the source parameter routine. The comparison with the smaller-$m$ LDT error uses its field-error floor $E>4^{-b'}/L$ and the bound $a'(dm)^{a'}2^{-b'md}\leq C/L$ for sufficiently large $n$, with $m\geq\lambda\mu n$ and $d=7$. Here $a',b'$ are the fixed seeded-LDT constants; the polynomial prefactor is absorbed into the exponential. It does not reverse the exponential inequality when $m'\geq m$. The quantitative chain is

$$
\kappa=O(\sqrt E+\rho),\qquad
\delta_3=O((\sqrt E+\rho)^{1/2}),\qquad
\mathrm{deficit}_{\mathrm{in}}=O(E^{1/16}+\rho^{1/8}).
$$

Choose a universal final exponent strictly below $\min\{b'/16,1/16\}$ and enlarge the polynomial coefficient and threshold to absorb every constant. This gives the displayed error of Theorem [Answer reduction](../part-09/thm-answer-reduction.md). When that error is at least one the value conclusion is trivial; the nontrivial regime also justifies the small-error inequalities above.

In the Lean, without the sandwich, the chain has one square root, from oracularization, and the exponent is $b=b'/2$. The field term $q^{-b'}$ of the low-degree test has the prefactor $a'(7m'(m'+6))^{a'}$, polynomial in $m'$ of degree about $2a'$, and is controlled by a hypothesis on the PCP decider, `FieldLarge`: for every exponent $e$, past a threshold on $Q$, its field has at least $(8(Q+1)m')^{e}$ elements; it is used at $e=40000(3\lceil a'\rceil+4)$, and a field of $2^{O(\log^2(Qm'))}$ elements satisfies it. Theorem [The bespoke PCP for deciders](../part-07/thm-pcp-decider.md) does not carry the paper's lower bound on $q$ (`eq:pcp-q-choice`); this is it, beside `ParamsBound` and `ShoupField`. The term $2^{-b'md}$ uses $m\geq Q$, from $2^m\geq 2T$, and the threshold on $n$; $\mu=0$ and $\varepsilon\geq 1$ are trivial, the loss being at least $1$ there. The constants are explicit, $a$ a function of the parameter polynomial alone and the threshold the larger of the two above, and the assembly is stated for a projective strategy in a bipartite model in which the seeded test is sound (`val_ge_of_arStrategy`), for every value model in which oracularization is sound and which dominates the model; the clause in $\mathrm{val}^*$ is its tensor-product case, and the clause in ${\omega^{\mathrm{co}}}$ (Theorem [Answer reduction is sound in ${\omega^{\mathrm{co}}}$, given the low-individual-degree test](../../downstream-results/part-03/thm-ar-sound-co.md)) the commuting-operator case, at the same constants.

## Depends on

- [Decoding with the original answer cutoff](lem-ar-decoding.md)
- [Typed soundness setup](lem-ar-soundness-setup.md)
- [Common individual polynomial measurements](lem-ar-common-polynomials.md)

## Proof depends on

- [Value models](../../downstream-results/part-01/def-value-model.md)
- [The low-individual-degree test is sound in the tensor-product model](../../downstream-results/part-03/lem-lidt-sound-in-tensor.md)

## Proof

With $\theta\leq 16^{54}\varepsilon$, the combined error is at most $39204\cdot16^{54}Z^{3A}\varepsilon^{b'}+(Q+1)^{-2}+22Z^{3A}2^{-b'Q}$, $Z=8(Q+1)m'$, $A=\lceil a'\rceil$, over the large field. The parameters bound $Z$ by a polynomial in $Q\sigma$, and $N^\mu\leq Q\leq N^{2\mu}$ for $N=\lambda n\geq2$, so $24\sqrt{7\,\mathrm{err}}$ is at most $\sigma^a(N^{\mu a}\varepsilon^{b'/2}+N^{-\mu b'/2})$ for a constant $a$ depending only on the parameter polynomial, past a threshold on $Q\geq n+1$.

## Lean

Formalized as [`MIPRE.AnswerReduction.arVerifier_soundness`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.arVerifier_soundness), [`MIPRE.AnswerReduction.FieldLarge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.FieldLarge), [`MIPRE.AnswerReduction.errE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.errE), [`MIPRE.AnswerReduction.errE_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.errE_le), [`MIPRE.AnswerReduction.sqrt_le_delta`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.sqrt_le_delta), [`MIPRE.AnswerReduction.exists_threshold_clB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.exists_threshold_clB), [`MIPRE.AnswerReduction.z_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.z_le), [`MIPRE.AnswerReduction.soundA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.soundA), [`MIPRE.AnswerReduction.soundC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.soundC), [`MIPRE.AnswerReduction.one_le_delta_of_trivial`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.one_le_delta_of_trivial), [`MIPRE.AnswerReduction.val_ge_of_arStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.val_ge_of_arStrategy), [`MIPRE.AnswerReduction.arVerifier_soundness_tensor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.arVerifier_soundness_tensor).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5951](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5951)
