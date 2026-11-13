---
declaration: section
origin: cited
lean: ModularFunction.IsMeromorphicAtInfty, ModularFunction.IsMeromorphicAtCusps, ModularFunction.IsMeromorphicOnH, ModularFunction.IsInvariantUnder, IsModularFunction
statement: formalized
proof: formalized
---

# Modular functions

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/modular-functions/index.html).

## Meromorphy at infinity

A function $f \colon \mathbb{H} \to \mathbb{C}$ on the upper
half-plane is meromorphic at infinity when there are a positive integer $N$ and a function
$g \colon \mathbb{C} \to \mathbb{C}$ meromorphic at $0$ such that
$f(\tau) = g(e^{2 \pi i \tau / N})$ for every $\tau \in \mathbb{H}$ with sufficiently large
imaginary part.

Formalized by `ModularFunction.IsMeromorphicAtInfty`, a definition declared in [MathlibExt/NumberTheory/ModularForms/MeromorphicAtCusps.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/MeromorphicAtCusps.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/modular-functions/index.html#is-meromorphic-at-infty).

## Meromorphy at the cusps

A function $f \colon \mathbb{H} \to \mathbb{C}$ on the upper
half-plane is meromorphic at the cusps when, for every $\gamma \in \mathrm{SL}(2, \mathbb{Z})$,
the function $\tau \mapsto f(\gamma \cdot \tau)$ is meromorphic at infinity, where $\gamma$ acts
on $\mathbb{H}$ by Möbius transformations.

Formalized by `ModularFunction.IsMeromorphicAtCusps`, a definition declared in [MathlibExt/NumberTheory/ModularForms/MeromorphicAtCusps.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/MeromorphicAtCusps.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/modular-functions/index.html#is-meromorphic-at-cusps).

## Meromorphy on the upper half-plane

A function $f \colon \mathbb{H} \to \mathbb{C}$ on
the upper half-plane is meromorphic when there is a function $g \colon \mathbb{C} \to \mathbb{C}$
that is meromorphic on the open set $\{z \in \mathbb{C} : \operatorname{Im} z > 0\}$ and
satisfies $g(\tau) = f(\tau)$ for every $\tau \in \mathbb{H}$.

Formalized by `ModularFunction.IsMeromorphicOnH`, a definition declared in [MathlibExt/NumberTheory/ModularForms/ModularFunction.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/ModularFunction.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/modular-functions/index.html#is-meromorphic-on-h).

## Invariance under a subgroup of the modular group

Let $\Gamma$ be a subgroup of
$\mathrm{SL}(2, \mathbb{Z})$. A function $f \colon \mathbb{H} \to \mathbb{C}$ on the upper
half-plane is invariant under $\Gamma$ when $f(\gamma \cdot \tau) = f(\tau)$ for every
$\gamma \in \Gamma$ and every $\tau \in \mathbb{H}$, where $\gamma$ acts on $\mathbb{H}$ by
Möbius transformations.

Formalized by `ModularFunction.IsInvariantUnder`, a definition declared in [MathlibExt/NumberTheory/ModularForms/ModularFunction.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/ModularFunction.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/modular-functions/index.html#is-invariant-under).

## Modular functions

Let $\Gamma$ be a subgroup of $\mathrm{SL}(2, \mathbb{Z})$. A function
$f \colon \mathbb{H} \to \mathbb{C}$ on the upper half-plane is a modular function for $\Gamma$
when it is meromorphic on $\mathbb{H}$, invariant under $\Gamma$, and meromorphic at the cusps.

No congruence hypothesis is assumed on $\Gamma$.

Formalized by `IsModularFunction`, a structure declared in [MathlibExt/NumberTheory/ModularForms/ModularFunction.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/ModularFunction.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/modular-functions/index.html#is-modular-function).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Modular functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/modular-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/modular-forms-q-series/modular-forms/modular-functions)
