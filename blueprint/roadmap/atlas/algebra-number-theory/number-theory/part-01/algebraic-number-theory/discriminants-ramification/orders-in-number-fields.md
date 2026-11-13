---
declaration: section
origin: cited
lean: NumberField.IsOrder.le_integralClosure, NumberField.IsOrder.isFractionRing, NumberField.IsOrder.exists_div_eq, NumberField.isOrder_integralClosure
statement: formalized
proof: formalized
---

# Orders in number fields

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/orders-in-number-fields/index.html).

## Orders lie in the ring of integers

Let $K$ be a number field and $O$ an order in $K$,
that is, a subring of $K$ contained in the ring of integers $\mathcal{O}_K$ (the integral
closure of $\mathbb{Z}$ in $K$) whose field of fractions is $K$. Then
$O \subseteq \mathcal{O}_K$.

Formalized by `NumberField.IsOrder.le_integralClosure`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Order.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Order.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/orders-in-number-fields/index.html#le-integral-closure).

## The fraction field of an order

Let $K$ be a number field and $O$ an order in $K$, that
is, a subring of $K$ contained in the ring of integers $\mathcal{O}_K$ (the integral closure of
$\mathbb{Z}$ in $K$) whose field of fractions is $K$. Then $K$, with the inclusion
$O \subseteq K$, is a field of fractions of $O$.

Formalized by `NumberField.IsOrder.isFractionRing`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Order.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Order.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/orders-in-number-fields/index.html#is-fraction-ring).

## Elements of a number field are quotients of elements of an order

Let $K$ be a number
field and $O$ an order in $K$, that is, a subring of $K$ contained in the ring of integers
$\mathcal{O}_K$ (the integral closure of $\mathbb{Z}$ in $K$) whose field of fractions is $K$.
Then for every $x \in K$ there are $a, b \in O$ with $b \neq 0$ and $x = a / b$.

Formalized by `NumberField.IsOrder.exists_div_eq`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Order.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Order.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/orders-in-number-fields/index.html#exists-div-eq).

## The ring of integers is an order

For every number field $K$, the ring of integers
$\mathcal{O}_K$, the integral closure of $\mathbb{Z}$ in $K$, is an order in $K$, that is, a
subring of $K$ contained in $\mathcal{O}_K$ whose field of fractions is $K$.

Formalized by `NumberField.isOrder_integralClosure`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Order.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Order.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/orders-in-number-fields/index.html#is-order-integral-closure).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Orders in number fields](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/orders-in-number-fields/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/orders-in-number-fields)
