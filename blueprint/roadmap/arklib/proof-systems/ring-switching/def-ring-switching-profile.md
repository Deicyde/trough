---
declaration: definition
origin: cited
lean: RingSwitching.RingSwitchingProfile
statement: formalized
---

# Ring-switching profile

Fix commutative rings $B$ (small) and $L$ (large) with $L$ a $B$-algebra, and $\kappa \in \mathbb{N}$. A *ring-switching profile* consists of:

- a rank-$2^\kappa$ $B$-basis $\beta = (\beta_u)_{u \in \{0,1\}^\kappa}$ of $L$;

- a commutative carrier ring $A$ (the type sent on the wire);

- two ring homomorphisms $\varphi_0, \varphi_1 : L \to A$ for evaluation-point data and polynomial coefficients, respectively, giving the scalar actions $x \cdot_0 z := \varphi_0(x)z$ and $x \cdot_1 z := \varphi_1(x)z$;

- coordinate maps $\mathrm{decomposeColumns}, \mathrm{decomposeRows} : A \to (\{0,1\}^\kappa \to L)$;

- subject to the two *reconstruction laws*

    $$
    z = \sum_{u} \varphi_0(\beta_u)\cdot \varphi_1(\mathrm{decomposeRows}(z)_u).\qquad\text{(1)}
    $$

    $$
    z = \sum_{v} \varphi_0(\mathrm{decomposeColumns}(z)_v)\cdot \varphi_1(\beta_v).\qquad\text{(2)}
    $$

    for all $z \in A$;

- the *row inverse law*: for every $c : \{0,1\}^\kappa \to L$,

    $$
    \mathrm{decomposeRows}\Bigl(\sum_{u} \varphi_0(\beta_u)\cdot \varphi_1(c_u)\Bigr) = c;
    $$

- and the *base compatibility* $\varphi_0(b) = \varphi_1(b)$ for $b \in B$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`RingSwitching.RingSwitchingProfile`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RingSwitching.RingSwitchingProfile).

## Sources

- [ArkLib blueprint: proof_systems/ring_switching.tex, line 23](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/ring_switching.tex#L23)
