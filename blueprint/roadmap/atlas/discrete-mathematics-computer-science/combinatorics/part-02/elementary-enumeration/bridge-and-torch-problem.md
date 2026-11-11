---
declaration: section
origin: cited
lean: MetaMathlibExt.BridgeTorchGeneralizations.bridgeWeight, MetaMathlibExt.BridgeTorchGeneralizations.bridgeWeight_small, MetaMathlibExt.BridgeTorchGeneralizations.bridgeWeight_of_seven_le, MetaMathlibExt.BridgeTorchGeneralizations.bridgeScheduleFrom, MetaMathlibExt.BridgeTorchGeneralizations.IsBridgeSchedule, MetaMathlibExt.BridgeTorchGeneralizations.scheduleCost, MetaMathlibExt.BridgeTorchGeneralizations.bridgeTime, MetaMathlibExt.BridgeTorchGeneralizations.forwardCrossings
statement: formalized
---

# Bridge and torch problem

48 results, 30 proved and 18 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html).

## Weights of the capacity-3 lower bound

The rational weights $y_i$ are
$y_1 = y_2 = y_3 = 0$, $y_4 = 2$, $y_5 = 4$, $y_6 = 5$, and $y_i = (4i - 8)/3$ for $i \ge 7$.
The value $y_0$ is unused and set to $0$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Lemma 15.

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.bridgeWeight`, a definition declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#bridge-weight).

## First seven weights of the capacity-3 lower bound

The weights $y_1, \dots, y_7$ of the
capacity-3 lower bound are $0, 0, 0, 2, 4, 5, 20/3$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Lemma 15.

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.bridgeWeight_small`, a theorem declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#bridge-weight-small).

## Weights of the capacity-3 lower bound from $7$ on

For every natural number $i \ge 7$,
the weight $y_i$ of the capacity-3 lower bound equals $(4i - 8)/3$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Lemma 15.

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.bridgeWeight_of_seven_le`, a theorem declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#bridge-weight-of-seven-le).

## Valid crossing sequences from a state of the bridge and torch problem

Let $c$ be a
natural number and let $P$ and $L$ be finite sets of natural numbers, the people and the left
bank. Whether a finite sequence $A_1, \dots, A_k$ of finite sets of natural numbers (the
crossings) is valid from the left bank $L$ with the torch on a given side is defined by recursion
on $k$. The empty sequence is valid exactly when $L = \emptyset$ and the torch is on the right.
With the torch on the left, the sequence is valid when $A_1$ is a nonempty subset of $L$ with at
most $c$ elements and $A_2, \dots, A_k$ is valid from the left bank $L \setminus A_1$ with the
torch on the right. With the torch on the right, it is valid when $A_1$ is a nonempty subset of
$P \setminus L$ with at most $c$ elements and $A_2, \dots, A_k$ is valid from the left bank
$L \cup A_1$ with the torch on the left.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, proof of Theorem 1 (states and moves) and Section 3 (capacity `c`).

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.bridgeScheduleFrom`, a definition declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#bridge-schedule-from).

## Bridge schedules

Let $c$ and $n$ be natural numbers. A finite sequence $\sigma$ of finite
sets of natural numbers (the crossings) is a schedule for the people $1, \dots, n$ on a bridge of
capacity $c$ with one torch when the following holds. Start with all of $1, \dots, n$ and the
torch on the left bank. The crossings at even positions (counting from $0$) are forward moves:
each is a nonempty set of at most $c$ people then on the left bank, who cross with the torch to
the right bank. The crossings at odd positions are returns: each is a nonempty set of at most $c$
people then on the right bank, who cross with the torch back to the left bank. After the last
crossing the left bank is empty and the torch is on the right bank.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, proof of Theorem 1 and Section 3.

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.IsBridgeSchedule`, a definition declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#is-bridge-schedule).

## Total time of a schedule

For a finite sequence $\sigma = (A_1, \dots, A_k)$ of finite sets
of natural numbers (the crossings), the total time of $\sigma$ is $\sum_{i=1}^{k} \max A_i$, where
$\max \emptyset = 0$. Since person $p$ has crossing time $p$, each crossing costs the largest
crossing time among the people in it.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, proof of Theorem 1.

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.scheduleCost`, a definition declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#schedule-cost).

## Optimal crossing time of the bridge and torch problem

For a bridge of capacity $c$ and
$n$ people $1, \dots, n$, where person $i$ has crossing time $i$, the optimal crossing time is
the least total time of a complete schedule with one torch; the total time of a schedule is the
sum, over its crossings, of the largest crossing time among the people in that crossing. It is
written $T(n)$ for $c = 2$ and $T_3(n)$ for $c = 3$. If no complete schedule exists (for
example when $n = 0$), the value is $0$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Theorem 1 and Theorem 12.

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.bridgeTime`, a definition declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#bridge-time).

## Forward crossings

The forward crossings of a list of crossings are its entries at the
even positions $0, 2, 4, \dots$ (counting from $0$), in their original order. For a schedule
these are its forward moves, from left to right.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Lemma 7.

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.forwardCrossings`, a definition declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#forward-crossings).

## Return crossings

For a list $\sigma = (A_0, A_1, \dots, A_{\ell - 1})$ whose entries may
come from any type, the returns of $\sigma$ are its entries at odd positions, $A_1, A_3, A_5, \dots$
in order, with positions counted from $0$. For the list of crossings of a bridge schedule these
are the crossings from right to left.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Lemma 7.

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.returnCrossings`, a definition declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#return-crossings).

## Right bank after a sequence of crossings

Let $n$ be a natural number and let
$\tau = (A_1, \dots, A_k)$ be a finite sequence of finite sets of natural numbers. The right bank
after $\tau$ is the set of those $p \in \{1, \dots, n\}$ for which the number of indices $i$ with
$p \in A_i$ is odd.

When $\tau$ is a prefix of a schedule for the people $1, \dots, n$, these are the people who have
crossed an odd number of times, so they stand on the right bank.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Lemma 9.

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.rightBank`, a definition declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#right-bank).

## Every schedule bounds the optimal time

For all natural numbers $c$ and $n$ and every
complete schedule $\sigma$ for the people $1, \dots, n$ on a bridge of capacity $c$ with one
torch, the optimal crossing time of these $n$ people on this bridge is at most the total time
of $\sigma$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Theorem 1 (definition of `T(n)`).

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.bridgeTime_le_scheduleCost`, a theorem declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#bridge-time-le-schedule-cost).

## A four-person schedule of total time 11

For the people $1, 2, 3, 4$ on a bridge of
capacity $2$, the crossings $\{1,2\}$ forward, $\{1\}$ back, $\{1,3\}$ forward, $\{1\}$ back,
$\{1,4\}$ forward, in this order, form a schedule, and its total time is $11$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, table after the proof of Theorem 1.

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.isBridgeSchedule_two_four`, a theorem declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#is-bridge-schedule-two-four).

## One crossing of three people under capacities two and three

For the people $1, 2, 3$,
the single forward crossing $\{1, 2, 3\}$ is not a schedule on a bridge of capacity $2$, but it
is a schedule on a bridge of capacity $3$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Section 3.

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.isBridgeSchedule_capacity_three`, a theorem declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#is-bridge-schedule-capacity-three).

## Forward moves, returns and right bank of a four-person schedule

For the schedule whose
crossings are, in order, $\{1,2\}$, $\{1\}$, $\{1,3\}$, $\{1\}$, $\{1,4\}$, the forward crossings
are $\{1,2\}, \{1,3\}, \{1,4\}$ and the returns are $\{1\}, \{1\}$. For the people $1, 2, 3, 4$,
the right bank after the crossings $\{1,2\}$, $\{1\}$ (the first two of the schedule) is $\{2\}$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, table after the proof of Theorem 1.

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.forwardCrossings_returnCrossings_rightBank_example`, a theorem declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#forward-crossings-return-crossings-right).

## Parity interpolation

Let $f, g, a : \mathbb{N} \to \mathbb{R}$ be sequences with
$a_{2m} = f(m)$ and $a_{2m+1} = g(m)$ for every $m \in \mathbb{N}$. Then for every
$n \in \mathbb{N}$,

$$a_n = \frac{1 + (-1)^n}{2} f(\lfloor n/2 \rfloor) + \frac{1 - (-1)^n}{2} g(\lfloor n/2 \rfloor).$$

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Lemma 2 (`jis-2026-26.5.6-lem-2`).

Stated but not proved: `MetaMathlibExt.BridgeTorchGeneralizations.parity_interpolation` is written with `theorem_wanted` in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#parity-interpolation).

## Local inequality for the capacity-3 weights

Let $y_i$ be the weights of the capacity-3
lower bound. For every nonempty set $T$ of positive integers with $|T| \le 3$,

$$\sum_{i \in T} y_i + \frac{9}{2}(|T| - 1) \le \max T + \sum_{i \in T} i.$$

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Lemma 15 (`jis-2026-26.5.6-lem-15`).

Stated but not proved: `MetaMathlibExt.BridgeTorchGeneralizations.bridgeWeight_local_inequality` is written with `theorem_wanted` in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#bridge-weight-local-inequality).

## Return inequality for the capacity-3 weights

Let $y_i$ be the weights of the capacity-3
lower bound. For every nonempty set $R$ of positive integers with $|R| \le 3$,

$$\frac{9}{2}(|R| - 1) + \max R + \sum_{i \in R} (y_i - i) \ge 0.$$

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Lemma 16 (`jis-2026-26.5.6-lem-16`).

Stated but not proved: `MetaMathlibExt.BridgeTorchGeneralizations.bridgeWeight_return_inequality` is written with `theorem_wanted` in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#bridge-weight-return-inequality).

## The capacity-3 closed form is an integer close to the lower bound

For every integer
$n \ge 7$, let $U(n) = n^2/6 + 2n - 181/36 + (-1)^n/4 - (2/9)\cos(2n\pi/3)$ and
$V(n) = n^2/6 + 2n - 11/2$. Then $U(n)$ is an integer and $0 \le U(n) - V(n) < 1$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Lemma 19 (`jis-2026-26.5.6-lem-19`), with `U` from Theorem 12 and `V` from Proposition 17.

Stated but not proved: `MetaMathlibExt.BridgeTorchGeneralizations.closedForm_U_integral_and_near_V` is written with `theorem_wanted` in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#closed-form-u-integral-and-near-v).

## Closed form for capacity two

Let $T(n)$ be the optimal crossing time of $n$ people with
crossing times $1, \dots, n$ on a bridge of capacity $2$ with one torch. For every $n \ge 2$,

$$T(n) = \frac{n^2}{4} + 3n - 5 + \frac{(-1)^n - 1}{8}.$$

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Theorem 1 (`jis-2026-26.5.6-thm-1`).

Stated but not proved: `MetaMathlibExt.BridgeTorchGeneralizations.bridgeTime_two_closed_form` is written with `theorem_wanted` in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#bridge-time-two-closed-form).

## Fewest crossings of the fastest person in an optimal schedule

For bridge capacity $2$
and $n \ge 1$ people $1, \dots, n$ (person $i$ has crossing time $i$), the least number $a(n)$
of crossings that include person $1$, taken over all optimal schedules (complete schedules
whose total time equals the optimal crossing time $T(n)$), is $a(n) = 2\lceil n/2 \rceil - 1$.
Crossings in both directions are counted.

This reads the paper's $a(n)$ as a minimum over optimal schedules (the paper discusses the
non-uniqueness of optimal schedules); over all schedules the minimum would be $1$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Proposition 6 (`jis-2026-26.5.6-prop-6`).

Stated but not proved: `MetaMathlibExt.BridgeTorchGeneralizations.bridgeTime_two_least_trips_of_fastest` is written with `theorem_wanted` in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#bridge-time-two-least-trips-of-fastest).

## Lower bound for capacity-two schedules

Let $n \ge 3$ and let $T(n)$ be the optimal
crossing time of the $n$ people $1, \dots, n$ (person $i$ crossing in time $i$) on a bridge of
capacity $2$. Let $\sigma$ be a bridge schedule of capacity $2$ for these people in which person
$1$ takes part in exactly $a$ forward moves, exactly $m$ returns carry two people and exactly $s$
forward moves carry one person. Then the total cost of $\sigma$ is at least
$T(n) + \lceil n/2 \rceil - a + 4m + 3s$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Lemma 7 (`jis-2026-26.5.6-lem-7`).

Stated but not proved: `MetaMathlibExt.BridgeTorchGeneralizations.scheduleCost_two_lower_bound` is written with `theorem_wanted` in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#schedule-cost-two-lower-bound).

## Initial values for capacity three

Let $T_3(n)$ be the optimal crossing time of $n$
people with crossing times $1, \dots, n$ on a bridge of capacity $3$ with one torch. Then
$T_3(1) = 1$, $T_3(2) = 2$, $T_3(3) = 3$, $T_3(4) = 7$, $T_3(5) = 9$ and $T_3(6) = 14$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Proposition 8 (`jis-2026-26.5.6-prop-8`).

Stated but not proved: `MetaMathlibExt.BridgeTorchGeneralizations.bridgeTime_three_initial_values` is written with `theorem_wanted` in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#bridge-time-three-initial-values).

## Optimal capacity-3 schedules with fastest single returns

Let $n \ge 1$ and consider the
people $1, \dots, n$, person $i$ having crossing time $i$, on a bridge of capacity $3$ with one
torch. Then some schedule has total time equal to the optimal crossing time $T_3(n)$ and the
following property: every return (a crossing at an odd position, counting from $0$) carries a
single person $p$, and $p \le q$ for every person $q$ on the right bank just before that return.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Lemma 9 (`jis-2026-26.5.6-lem-9`).

Stated but not proved: `MetaMathlibExt.BridgeTorchGeneralizations.exists_optimal_schedule_three_fastest_returns` is written with `theorem_wanted` in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#exists-optimal-schedule-three-fastest-re).

## Six-step upper bound for capacity three

Let $T_3(n)$ be the optimal crossing time of
$n$ people with crossing times $1, \dots, n$ on a bridge of capacity $3$ with one torch. For
every $k \ge 9$, $T_3(k) \le T_3(k - 6) + 2k + 6$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Proposition 11 (`jis-2026-26.5.6-prop-11`).

Stated but not proved: `MetaMathlibExt.BridgeTorchGeneralizations.bridgeTime_three_le_sub_six` is written with `theorem_wanted` in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#bridge-time-three-le-sub-six).

## Upper bound for capacity three

Let $T_3(n)$ be the optimal crossing time of $n$ people
with crossing times $1, \dots, n$ on a bridge of capacity $3$ with one torch. For every
$n \ge 7$,

$$T_3(n) \le \frac{n^2}{6} + 2n - \frac{181}{36} + \frac{(-1)^n}{4} - \frac{2}{9}\cos(2n\pi/3).$$

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Theorem 12 (`jis-2026-26.5.6-thm-12`).

Stated but not proved: `MetaMathlibExt.BridgeTorchGeneralizations.bridgeTime_three_le_closed_form` is written with `theorem_wanted` in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#bridge-time-three-le-closed-form).

## Lower bound for capacity-three schedules

Let $n \ge 7$. Every bridge schedule of
capacity $3$ for the $n$ people $1, \dots, n$ (person $i$ crossing in time $i$) has total cost at
least $V(n) = n^2/6 + 2n - 11/2$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Proposition 17 (`jis-2026-26.5.6-prop-17`).

Stated but not proved: `MetaMathlibExt.BridgeTorchGeneralizations.scheduleCost_three_lower_bound` is written with `theorem_wanted` in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#schedule-cost-three-lower-bound).

## Closed form for capacity three

Let $T_3(n)$ be the optimal crossing time of $n$ people
with crossing times $1, \dots, n$ on a bridge of capacity $3$ with one torch. For every
$n \ge 7$,

$$T_3(n) = \frac{n^2}{6} + 2n - \frac{181}{36} + \frac{(-1)^n}{4} - \frac{2}{9}\cos(2n\pi/3).$$

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Theorem 20 (`jis-2026-26.5.6-thm-20`).

Stated but not proved: `MetaMathlibExt.BridgeTorchGeneralizations.bridgeTime_three_closed_form` is written with `theorem_wanted` in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#bridge-time-three-closed-form).

## Six-step recurrence for capacity three

Let $T_3(n)$ be the optimal crossing time of
$n$ people with crossing times $1, \dots, n$ on a bridge of capacity $3$ with one torch. For
every $n \ge 13$, $T_3(n) = T_3(n - 6) + 2n + 6$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Corollary 21 (`jis-2026-26.5.6-cor-21`).

Stated but not proved: `MetaMathlibExt.BridgeTorchGeneralizations.bridgeTime_three_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#bridge-time-three-recurrence).

## Admissible bags

Let $n$ be a natural number. A finite multiset $F$ of finite sets of
natural numbers is an admissible bag for $n$ people (bridge capacity $3$) when (i) every $T \in F$
is a nonempty subset of $\{1, \dots, n\}$ with $|T| \le 3$, (ii) every $i \in \{1, \dots, n\}$
lies in some $T \in F$, and (iii) $\sum_{T \in F} (|T| - 1) = n - 1$, where the sum counts each
member of $F$ with its multiplicity and $n - 1$ is read as $0$ when $n = 0$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Definition (admissible bag), Section 3 (journal version).

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.IsAdmissibleBag`, a definition declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#is-admissible-bag).

## Weight of a bag

For a natural number $n$ and a bag $F$, that is, a finite multiset of
finite sets of natural numbers, the weight of $F$ for $n$ people is the real number
$w(F) = \sum_{T \in F} \left(\max T + \sum_{i \in T} i\right) - \frac{n(n+1)}{2}$, where each
set counts with its multiplicity in $F$ and $\max \emptyset = 0$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Definition (admissible bag), Section 3 (journal version).

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.bagWeight`, a definition declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#bag-weight).

## A one-trip admissible bag for three people

The multiset whose only member is the set
$\{1, 2, 3\}$ is an admissible bag for $3$ people, and its weight for $3$ people is $3$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Definition (admissible bag), characteristic example.

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.isAdmissibleBag_three_and_bagWeight`, a theorem declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#is-admissible-bag-three-and-bag-weight).

## Schedules with single-person returns give admissible bags

Let $n$ be a natural number
and let $\sigma$ be a schedule for the people $1, \dots, n$ on a bridge of capacity $3$ in which
every return carries exactly one person. Let $F(\sigma)$ be the multiset of the forward crossings
of $\sigma$. Then $F(\sigma)$ is an admissible bag for $n$ people, and the total time of $\sigma$
equals the weight $w(F(\sigma))$ of this bag for $n$ people.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Proposition 14 (`jis-2026-26.5.6-prop-14`), first assertion.

Stated but not proved: `MetaMathlibExt.BridgeTorchGeneralizations.isAdmissibleBag_forwardCrossings_of_single_returns` is written with `theorem_wanted` in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#is-admissible-bag-forward-crossings-of-s).

## Some admissible bag weighs at most the capacity-3 optimal time

For every natural number
$n$, some admissible bag $F$ for $n$ people has weight $w(F)$ at most the capacity-3 optimal
crossing time $T_3(n)$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Proposition 14 (`jis-2026-26.5.6-prop-14`), consequence.

Stated but not proved: `MetaMathlibExt.BridgeTorchGeneralizations.exists_isAdmissibleBag_bagWeight_le_bridgeTime_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 412](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L412). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#exists-is-admissible-bag-bag-weight-le-b).

## Lower bound for the weight of an admissible bag

For every natural number $n \ge 7$
and every admissible bag $F$ for $n$ people, the weight of $F$ is at least
$\frac{n^2}{6} + 2n - \frac{11}{2}$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Corollary 18 (`jis-2026-26.5.6-cor-18`).

Stated but not proved: `MetaMathlibExt.BridgeTorchGeneralizations.bagWeight_ge_of_isAdmissibleBag` is written with `theorem_wanted` in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#bag-weight-ge-of-is-admissible-bag).

## Movement in the star model

Consider the star graph $\mathcal{S}(k)$ with center $o$ and
leaves $u_0, \dots, u_{k-1}$, and $n$ persons $0, \dots, n-1$, where person $p$ has crossing time
$p + 1$. A movement consists of a set $P$ of persons, a leaf $u_j$ and a direction: the persons in
$P$ carry one torch along the edge $\{o, u_j\}$, outward from $o$ to $u_j$ or inward from $u_j$ to
$o$. No condition is imposed on $P$ here (it may even be empty); which movements may be made
together is part of the definition of a legal step.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Definition (the star model), Section 5 (journal version).

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.StarMove`, a structure declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 433](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#star-move).

## Start vertex of a star movement

Let $\mathcal{S}(k)$ be the star graph with center $o$
and $k$ leaves. A movement in the star model on $\mathcal{S}(k)$ along the edge $\{o, u\}$ between
the center $o$ and a leaf $u$ starts at $o$ if it goes outward (from the center to the leaf) and
at $u$ otherwise.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Definition (the star model).

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.StarMove.src`, a definition declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#src).

## End vertex of a star movement

In the star model on the star graph with center $o$ and
leaves $u_0, \dots, u_{k-1}$, a torch-movement along the edge $\{o, u_\ell\}$ ends at the leaf
$u_\ell$ if it goes outward from $o$, and at the center $o$ otherwise.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Definition (the star model).

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.StarMove.dst`, a definition declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#dst).

## Legal parallel steps in the star model

Let $\mathcal{S}(k)$ be the star graph with a
center and $k$ leaves. Consider a configuration of the star model on $\mathcal{S}(k)$ with $n$
persons, given by the vertex $\mathrm{pos}(p)$ of each person $p$ and the number $\mathrm{tor}(v)$
of torches at each vertex $v$. A parallel step, a list of star movements, is legal from this
configuration when every movement carries one or two persons, all standing at the movement's
start vertex; the movements of the step carry pairwise disjoint sets of persons and traverse
pairwise distinct edges; and for every vertex $v$, at most $\mathrm{tor}(v)$ movements of the
step start at $v$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Definition (the star model).

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.IsStarStep`, a definition declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 466](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#is-star-step).

## Positions after a step in the star model

Given the vertex $\mathrm{pos}(p)$ of each person
$p$ and a step $S$, a finite list of movements, the position of $p$ after $S$ is the end vertex of
the first movement of $S$ whose persons include $p$ (its leaf if the movement is outward, the
center if it is inward), and $\mathrm{pos}(p)$ if no movement of $S$ includes $p$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Definition (the star model).

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.starStepPos`, a definition declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 481](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L481). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#star-step-pos).

## Torch counts after a step in the star model

Given the number $\mathrm{tor}(v)$ of torches
at each vertex $v$ of the star graph and a step $S$, a finite list of movements, the number of
torches at $v$ after $S$ is $\max(\mathrm{tor}(v) - a, 0) + b$, where $a$ is the number of
movements of $S$ that start at $v$ and $b$ is the number of movements of $S$ that end at $v$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Definition (the star model).

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.starStepTorch`, a definition declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 492](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L492). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#star-step-torch).

## Duration of a step in the star model

A step is a finite list of movements carried out in
parallel. Its duration is the largest crossing time $p + 1$ of a person $p$ moving in one of its
movements, and $0$ if no person moves.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Definition (the star model).

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.starStepDuration`, a definition declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#star-step-duration).

## Legal runs in the star model

A configuration of the star model assigns to each person $p$
a vertex $\mathrm{pos}(p)$ of the star graph $\mathcal{S}(k)$ and to each vertex $v$ a number
$\mathrm{tor}(v)$ of torches. A finite sequence $\sigma = (S_1, \dots, S_\ell)$ of steps, each a
finite list of movements, is a legal run from the configuration $(\mathrm{pos}, \mathrm{tor})$
when each step $S_i$ is legal from the configuration reached after $S_1, \dots, S_{i-1}$ (a step
updates the positions of the persons and the torch counts) and every person is at a leaf in the
configuration reached after all of $\sigma$. In particular, the empty sequence is a legal run
exactly when every person already stands at a leaf.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Definition (the star model).

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.starRunFrom`, a definition declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 511](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L511). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#star-run-from).

## Star schedules

Consider the star model on the star graph $\mathcal{S}(k)$, which has a
center and $k$ leaves, with $n$ persons and $t$ torches. A finite list $\sigma$ of parallel steps
(each a list of star movements) is a star schedule when the following holds. Start from the
configuration with every person and all $t$ torches at the center and no torch at any leaf, and
apply the steps of $\sigma$ in order, where a step moves the persons of each of its movements to
the movement's end vertex and moves one torch from the start vertex to the end vertex of each
movement. Every step must be legal from the configuration it is applied to, and in the final
configuration every person is at some leaf.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Definition (the star model).

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.IsStarSchedule`, a definition declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 524](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L524). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#is-star-schedule).

## Optimal time in the star model

For $n$ persons, $k$ edges and $t$ torches, $T(n, k, t)$
is the smallest total duration of a star schedule, where the total duration of a schedule is the
sum of the durations of its steps. If no star schedule exists (for example when $n \ge 1$ and
$k = 0$ or $t = 0$), then $T(n, k, t) = 0$ by convention.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Definition (the star model).

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.starTime`, a definition declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 532](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L532). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#star-time).

## Every star schedule bounds the optimal time

Let $T(n, k, t)$ be the optimal time of
the star model with $n$ persons, $k$ edges and $t$ torches. For every star schedule $\sigma$ with
$n$ persons, $k$ edges and $t$ torches, $T(n, k, t)$ is at most the total duration of $\sigma$,
the sum of the durations of its steps.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Definition (the star model), definition of `T(n, k, t)`.

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.starTime_le`, a theorem declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 540](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L540). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#star-time-le).

## Two persons crossing a one-edge star

In the star model with $2$ persons (crossing times
$1$ and $2$), a star graph with $1$ edge and $1$ torch, the sequence of one step consisting of a
single movement that carries both persons and the torch from the center to the leaf is a star
schedule, and its total duration is $2$.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Definition (the star model), characteristic example.

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.isStarSchedule_two_one_one`, a theorem declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 550](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L550). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#is-star-schedule-two-one-one).

## Example: no return from a leaf without a torch

In the star model on the star graph
with a center and a single leaf, with one person, suppose the person stands at the leaf, the only
torch is at the center and no torch is at the leaf. Then the parallel step consisting of the
single movement that carries the person from the leaf back to the center is not legal.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Definition (the star model), characteristic example.

Formalized by `MetaMathlibExt.BridgeTorchGeneralizations.not_isStarStep_return_without_torch`, a theorem declared in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 562](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L562). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#not-is-star-step-return-without-torch).

## Bridge and torch on star graphs

Consider the star model with $n \ge 2$ persons of crossing
times $1, \dots, n$, $k \ge 1$ edges and $t \ge 1$ torches, let $T(n, k, t)$ be its optimal time,
and let $m = \min(k, t)$ and $s = \lceil n/(2m) \rceil$. Let $T(n)$ be the optimal crossing time
of $n$ persons with crossing times $1, \dots, n$ on a bridge of capacity $2$ with one torch. Then

$$sn - ms(s-1) \le T(n, k, t) \le T(n),$$

and the left inequality is an equality whenever $t \ge \lceil n/2 \rceil$. Moreover, for all
natural numbers $q$ and $r$ with $n = 2mq + r$ and $r < 2m$,

$$sn - ms(s-1) = \frac{n^2}{4m} + \frac{n}{2} + \frac{r(2m-r)}{4m},$$

and this is at least $n^2/(4m) + n/2$.

For $n \ge 2$ the closed form $T(n) = n^2/4 + 3n - 5 + ((-1)^n - 1)/8$ is Theorem 1 of the same
paper.

## Sources

- Thang Pang Ern and Gerard Sayson, *Some Generalizations of the Bridge and Torch Problem*, Journal of Integer Sequences 29 (2026), Article 26.5.6, Theorem 26 (`jis-2026-26.5.6-thm-26`).

Stated but not proved: `MetaMathlibExt.BridgeTorchGeneralizations.starTime_bounds` is written with `theorem_wanted` in [WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean, line 579](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BridgeTorchGeneralizationsWanted.lean#L579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html#star-time-bounds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bridge and torch problem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/elementary-enumeration/bridge-and-torch-problem)
