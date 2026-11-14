---
declaration: definition
origin: cited
lean: ConNF.CoherentData
statement: formalized
---

# coherent data

Let $\alpha$ be a proper type index. Suppose that we have model data for all type indices $\beta \leq \alpha$, position functions for $\mathsf{Tang}_\beta$ for all $\beta < \alpha$, and typed near-litters for all $\beta < \alpha$. We say that the model data is *coherent* below level $\alpha$ if the following hold.

- For $\gamma < \beta \leq \alpha$, there is a map $\mathsf{AllPerm}_\beta \to \mathsf{AllPerm}_\gamma$ that commutes with the coercions from $\mathsf{AllPerm}_{(-)}$ to $\mathsf{StrPerm}_{(-)}$. We can use this map to define arbitrary derivatives of allowable permutations by recursion on paths.

- If $(x, S)$ is a $\beta$-tangle for $\beta < \alpha$, and $y$ is an atom or near-litter that occurs in the range of $S_A$, then $\iota(y) < \iota(x, S)$.

- Let $\beta \leq \alpha$, and let $\gamma, \delta < \beta$ be distinct with $\delta$ proper. Let $t : \mathsf{Tang}_\gamma$ and $\rho : \mathsf{AllPerm}_\beta$. Then

    $$
    (\rho_\delta)_\bot(f_{\gamma,\delta}(t)) = f_{\gamma,\delta}(\rho_\gamma(t))
    $$

    In particular, for every $\beta \leq \alpha$, $\beta$-allowable permutation $\rho$, and $\beta$-inflexible path $I$, we obtain

    $$
    ((\rho_A)_\varepsilon)_\bot(f_{\delta,\varepsilon}(t)) = f_{\delta,\varepsilon}((\rho_A)_\delta(t))
    $$

    where subscripts of $I$ are suppressed.

- Suppose that $\beta \leq \alpha$ and $(\rho(\gamma))_{\gamma < \beta}$ is a collection of allowable permutations such that whenever $\gamma, \delta < \beta$ are distinct, $\delta$ is proper, and $t : \mathsf{Tang}_\delta$, we have

    $$
    (\rho(\delta))_\bot(f_{\gamma,\delta}(t)) = f_{\gamma,\delta}(\rho(\gamma)(t))
    $$

    Then there is a $\beta$-allowable permutation $\rho$ with $\rho_\gamma = \rho(\gamma)$ for each $\gamma < \beta$.

- If $\beta \leq \alpha$ is a proper type index and $x : \mathsf{TSet}_\beta$, then for any $\gamma < \beta$,

    $$
    U_\beta(x)(\gamma) \subseteq \operatorname{\mathsf{ran}} U_\gamma
    $$

- (extensionality) If $\beta, \gamma \leq \alpha$ are proper type indices where $\gamma < \beta$, the map $U_\beta(-)(\gamma) : \mathsf{TSet}_\beta \to \operatorname{\mathsf{Set}} \mathsf{StrSet}_\gamma$ is injective.

- If $\beta, \gamma : \lambda$ where $\gamma < \beta$, for every $x : \mathsf{TSet}_\gamma$ there is some $y : \mathsf{TSet}_\beta$ such that $U_\beta(y)(\gamma) = \{ x \}$. We write $\operatorname{\mathsf{singleton}}_\beta(x)$ for this object $y$, which is uniquely defined by extensionality.

Note that this structure contains data (the derivative maps for allowable permutations and the singleton operations), but the type is a subsingleton: any two inhabitants are propositionally equal. We will not use this fact directly, but the idea will have relevance in [Wrapping up the main induction](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/content.tex#L21).

## Depends on

- [typed near-litter](def-typednearlitter.md)
- [inflexible path](def-inflexiblepath.md)

## Lean

Formalized as [`ConNF.CoherentData`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.CoherentData).

## Sources

- [Consistency of New Foundations blueprint: chapters/environment.tex, line 418](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/environment.tex#L418)
