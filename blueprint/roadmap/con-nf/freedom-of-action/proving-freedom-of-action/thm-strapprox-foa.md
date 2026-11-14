---
declaration: theorem
origin: cited
lean: ConNF.StrApprox.exists_exactlyApproximates
statement: formalized
proof: formalized
---

# freedom of action

Freedom of action holds at all type indices $\beta \leq \alpha$.

## Depends on

- [freedom of action](def-freedomofaction.md)

## Proof depends on

- [StrApprox.chain](prop-strapprox-chain.md)
- [adding flexible litters](prop-strapprox-addflexible.md)
- [coherent data](../../setting-up-the-environment/hypotheses-of-the-recursion/def-coherentdata.md)

## Proof

By induction, we may assume freedom of action holds at all $\delta < \beta$. Let $\psi$ be a coherent $\beta$-approximation, and let $\chi$ be a maximal coherent extension, which exists by Zorn's lemma and [Proposition StrApprox.chain](prop-strapprox-chain.md).

Suppose that there is a litter $L$ such that there exists a path $A$ where $L \notin \operatorname{\mathsf{coim}} \chi_A^{\mathcal L}$. Let $L$ have minimal position with this property, and let $A$ be such a path.

Suppose that $L$ is $A$-flexible. Then by [adding flexible litters](prop-strapprox-addflexible.md), there is an extension $\varphi$ of $\chi$ such that $L \in \operatorname{\mathsf{coim}} \varphi_A^{\mathcal L}$, contradicting maximality of $\chi$.

Suppose that $L$ is $A$-inflexible, with path $(\gamma,\delta,\varepsilon,B)$ and tangle $t$. Then $(\psi_B)_\delta$ is defined on all of $\operatorname{\mathsf{supp}}(t)$. Indeed, by [coherent data](../../setting-up-the-environment/hypotheses-of-the-recursion/def-coherentdata.md) (coherent data) and [fuzz maps](../../setting-up-the-environment/hypotheses-of-the-recursion/prop-fuzz.md) (fuzz maps), for each atom or near-litter $y$ that appears in the range of $\operatorname{\mathsf{supp}}(t)_C$, we have $\iota(y) < \iota(t) < \iota(L)$, giving the desired conclusion by minimality of the position of $L$ and the criteria of [base positions](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/environment.tex#L320). Thus, we obtain the same contradiction by [adding inflexible litters](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L321).

So $\operatorname{\mathsf{coim}} \chi_A^{\mathcal L}$ is the set of all litters for each path $A$. We then use the fact that our model data is coherent to recursively compute the allowable permutation $\rho$ with the same action as $\chi$. Then $\chi$ exactly approximates $\rho$, so $\psi$ also exactly approximates $\rho$. (In general, if $\psi \leq \chi$ and $\chi$ (exactly) approximates $\rho$ then $\psi$ (exactly) approximates $\rho$.)

## Lean

Formalized as [`ConNF.StrApprox.exists_exactlyApproximates`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.StrApprox.exists_exactlyApproximates).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 367](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L367)
