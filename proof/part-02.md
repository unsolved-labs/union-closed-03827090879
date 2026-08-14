First work in the open region \(j(y)<1/2\). Put \(z=J(x,y)\). Then \(z<1/2\), so \(\ell'(z)>0\), and

\[
G_{xy}=\ell''(z)J_xJ_y+\ell'(z)J_{xy}.
\]

It is enough to establish

\[
-\frac{z\ell''(z)}{\ell'(z)}
\ge \frac1{1-z}
\ge \frac{zJ_{xy}}{J_xJ_y}.
\tag{4.2}
\]

#### Entropy side of (4.2)

Let

\[
a=\log\frac{1-z}{z}>0.
\]

A direct calculation gives

\[
-\frac{z\ell''(z)}{\ell'(z)}
=
\frac1{(1-z)a}+\frac{za}{h(z)}.
\tag{4.3}
\]

After multiplication by the positive denominator \(h(z)(1-z)a\), the desired difference has numerator

\[
N=h(z)(1-a)+za^2(1-z).
\]

For \(0<a\le1\), this is immediately nonnegative. For \(a\ge1\), use

\[
h(z)=za-\log(1-z)
\le z\left(a+\frac1{1-z}\right).
\]

Because \(1-a\le0\), this upper bound yields

\[
N\ge \frac{z}{1-z}\left[1-za\bigl(1+(1-z)a\bigr)\right].
\]

Since \(z=1/(1+e^a)<e^{-a}\), it is enough that

\[
a(1+a)e^{-a}\le1,
\]

or \(e^a\ge a+a^2\). The latter follows, for example, from the Taylor expansion of \(e^a\); indeed

\[
1+a+\frac{a^2}{2}+\frac{a^3}{6}\ge a+a^2
\]

because \(a^3-3a^2+6>0\) for \(a\ge0\).

#### Geometric side of (4.2)

Direct algebra gives

\[
J_xJ_y-(1-J)JJ_{xy}=x^2y^2P(x,y),
\tag{4.4}
\]

where

\[
\begin{aligned}
P(x,y)={}&4x^3y^3-10x^3y^2+8x^3y-2x^3
-10x^2y^3+34x^2y^2-34x^2y+10x^2\\
&+8xy^3-34xy^2+44xy-16x
-2y^3+10y^2-16y+7.
\end{aligned}
\]

Moreover,

\[
j\left(\frac{84}{125}\right)-\frac12
=\frac{81647}{488281250}>0.
\]

Because \(j\) is increasing, \(j(y)\le1/2\) implies \(x,y\le84/125\). Rescale

\[
x=\frac{84}{125}r,\qquad y=\frac{84}{125}s,
\qquad 0\le r,s\le1.
\]

The tensor-product Bernstein coefficients of bidegree \((3,3)\) are

\[
\begin{pmatrix}
7 & \frac{427}{125} & \frac{4179}{3125} & \frac{306467}{1953125}\\[3pt]
\frac{427}{125} & \frac{31871}{15625} & \frac{1996771}{1953125} & \frac{73410071}{244140625}\\[3pt]
\frac{4179}{3125} & \frac{1996771}{1953125} & \frac{168517111}{244140625} & \frac{2226969759}{6103515625}\\[3pt]
\frac{306467}{1953125} & \frac{73410071}{244140625} & \frac{2226969759}{6103515625} & \frac{1418724425839}{3814697265625}
\end{pmatrix}.
\]

Every coefficient is positive. Bernstein basis functions are nonnegative and sum to one, hence \(P>0\) on the square. This proves the second inequality in (4.2), then \(G_{xy}\le0\), then \(R_y\ge0\), and finally (2.1) when \(j(y)<1/2\). The boundary \(j(y)=1/2\) follows by continuity.

The script `verify_auxiliary_inequality.py` reproduces (4.4), the exact value of \(j(84/125)-1/2\), and all sixteen Bernstein coefficients using only `fractions.Fraction`.

## 5. Normalized form of Lemma 2

For \(t\in(0,1)\), define

\[
u(t)=\frac{h(t)}t,
\qquad
v(t)=\frac{\sqrt{h(j(t))}}t.
\]

After division by \(xy\), (2.2) is equivalent to

\[
\Delta(x,y):=
\alpha u(xy)+\beta v(x)v(y)-\kappa\bigl(u(x)+u(y)\bigr)\ge0.
\tag{5.1}
\]

The function is symmetric. The proof divides the square into three regions:

1. a small-variable strip, \(\min(x,y)\le0.01\);
2. a compact core, \(0.01\le x,y\le0.999999\);
3. a near-one strip, \(\max(x,y)\ge0.999999\).

## 6. Hand proofs on the boundary strips

### 6.1. The strip \(0<x\le0.01\)

For \(0<x,y\le1\),

\[
u(xy)\ge u(x)-\log y.
\tag{6.1}
\]

To see this, put \(g(t)=u(e^{-t})\). Since

\[
g'(t)=\frac{-\log(1-e^{-t})}{e^{-t}}\ge1,
\]

(6.1) follows by integration.

For \(x\le0.01\),

\[
j(x)\ge\frac{19801}{10000}x^2,
\qquad
j(x)\le2x^2\le\frac1{5000}.
\]

Since \(h(z)\ge z\log(1/z)\) and \(\log5000>8\),

\[
v(x)^2\ge\frac{19801}{10000}\log5000>\frac{49}{4},
\]

so \(v(x)>7/2\). Since \(\beta>1/10\),
\[
\beta v(x)v(y)\ge\frac7{20}v(y).
\]

Using that \(u\) is decreasing and \(\alpha-\kappa>0\), (5.1) is bounded below by

\[
(\alpha-\kappa)u(0.01)+R(y),
\]

where

\[
R(y)=-\alpha\log y-\kappa u(y)+\frac7{20}v(y).
\tag{6.2}
\]

It remains to show \(R(y)\ge0\).

* If \(0<y\le10^{-4}\), then \(u(y)\le1-\log y\) and \(-\log y>46/5\), so
  \[
  -\alpha\log y-\kappa u(y)
  \ge\frac{46}{5}(\alpha-\kappa)-\kappa
  =\frac{3396956229022569}{192903410031250000}>0.
  \]

* If \(0.9999\le y<1\), put \(\varepsilon=1-y\) and \(r=1-j(y)\). Then \(r\ge\varepsilon\) and both are below \(1/2\), hence
  \[
  \frac{v(y)}{u(y)}
  =\frac{\sqrt{h(r)}}{h(\varepsilon)}
  \ge\frac1{\sqrt{h(\varepsilon)}}.
  \]
  Also
  \[
  h(\varepsilon)\le\varepsilon(1-\log\varepsilon)
  \le\frac{11}{10000},
  \]
  using \(\log10000<10\). Consequently \((7/20)v(y)>\kappa u(y)\), so \(R(y)\ge-\alpha\log y\ge0\).

* On \([10^{-4},0.9999]\), `verify_R()` proves \(R>0\) by interval Taylor bounds. It terminates with 39 certified boxes and a least per-box lower bound of
  \[
  0.0033854057973891488.
  \]

Thus the entire small-variable strip is certified.

### 6.2. The strip \(y\ge0.999999\)

By symmetry assume \(x\le y\), and suppose \(x>0.01\).

If \(x\le0.998\), then \(u(xy)\ge u(x)\), so after dropping the nonnegative \(v\)-term,

\[
\Delta(x,y)
\ge(\alpha-\kappa)u(0.998)-\kappa u(0.999999)>0.
\tag{6.3}
\]

The directed-rounding lower bound in the checker is

\[
0.0012884232397950039.
\]

It remains to treat \(0.998\le x\le y<1\). The function \(g(t)=u(e^{-t})\) is concave because, with \(z=e^{-t}\),

\[
g''(t)=-\frac{z/(1-z)+\log(1-z)}z<0.
\]

Therefore

\[
u(xy)\ge\frac{u(x^2)+u(y^2)}2.
\tag{6.4}
\]

It is enough to prove

\[
\alpha u(z^2)>2\kappa u(z),
\qquad 0.998\le z<1.
\tag{6.5}
\]

Write \(z=1-\varepsilon\), where \(0<\varepsilon\le1/500\), and put

\[
r=1-z^2=2\varepsilon-\varepsilon^2,
\qquad L=-\log\varepsilon.
\]

Use

\[
h(t)=t(1-\log t)-E(t),
\qquad
0\le E(t)\le\frac{t^2}{2(1-t)}.
\tag{6.6}
\]

Multiplying the left side of (6.5) by the positive factor \(z^2/\varepsilon\), (6.6) gives the lower bound

\[
\begin{aligned}
&[\alpha(2-\varepsilon)-2\kappa(1-\varepsilon)](1+L)
-\alpha(2-\varepsilon)\log(2-\varepsilon)\\
&\hspace{40mm}
-\frac{\alpha\varepsilon(2-\varepsilon)^2}{2(1-r)}.
\end{aligned}
\tag{6.7}
\]

The following elementary bounds hold:

\[
\alpha(2-\varepsilon)-2\kappa(1-\varepsilon)>\frac{1799}{10000},
\]

\[
L\ge\log500>\frac{31}{5},
\qquad
\log(2-\varepsilon)<\log2<\frac7{10},
\]

and

\[
\frac{\alpha\varepsilon(2-\varepsilon)^2}{2(1-r)}<\frac1{250}.
\]

Thus (6.7) is greater than

\[
\frac{1799}{10000}\left(1+\frac{31}{5}\right)
-\frac9{10}\cdot2\cdot\frac7{10}
-\frac1{250}
=\frac{391}{12500}>0.
\]

This proves the near-one strip.

## 7. Directed-rounding proof on the compact core

It remains to prove

\[
\Delta(x,y)\ge0
\qquad
\text{on }
[0.01,0.999999]^2.
\tag{7.1}
\]

The checker uses Boost.Interval with IEEE-754 directed rounding. It does not call the system logarithm. For \(1\le q\le2\), put \(w=(q-1)/(q+1)\); then

\[
\log q
=2\sum_{n=0}^{N}\frac{w^{2n+1}}{2n+1}+R_N,
\]

with

\[
0\le R_N\le
\frac{2w^{2N+3}}{(2N+3)(1-w^2)}.
\]

The code uses \(N=24\) after exact binary exponent extraction by `frexp`.

The derivative formulas used in the Taylor bounds are

\[
u'(t)=\frac{\log(1-t)}{t^2},
\]

\[
u''(t)=-\frac1{t^2(1-t)}-\frac{2\log(1-t)}{t^3}.
\]

For

\[
q(t)=h(j(t)),
\qquad
v(t)=\frac{\sqrt{q(t)}}t,
\]

let

\[
