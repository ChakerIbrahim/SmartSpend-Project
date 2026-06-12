const CSRF = document.querySelector('meta[name="csrf-token"]').content;

        async function api(endpoint, data) {
            const res = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': CSRF,
                },
                body: JSON.stringify(data),
            });
            const json = await res.json();
            return { ok: res.ok, status: res.status, data: json };
        }

        function setLoading(btnId, loading, loadingText) {
            const btn = document.getElementById(btnId);
            if (!btn) return;
            btn.disabled = loading;
            if (loading) {
                btn.dataset.orig = btn.textContent;
                btn.innerHTML = `<svg class="w-4 h-4 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"/></svg>${loadingText}`;
            } else {
                btn.innerHTML = btn.dataset.orig || btn.textContent;
            }
        }

        function showBanner(id, msgId, message) {
            document.getElementById(id).classList.remove('hidden');
            if (msgId) document.getElementById(msgId).textContent = message;
        }
        function hideBanner(id) { document.getElementById(id).classList.add('hidden'); }

        function setInputState(input, state) {
            input.classList.remove('error', 'success');
            if (state) input.classList.add(state);
        }

        // ─── Screen navigation ──────────────────────────────────────────────────────
        function show(id) {
            document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
            document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
            document.getElementById(id).classList.add('active');
            const map = { login: 0, register: 1, forgot: 2, reset: 3, verify: 4, success: 5 };
            document.querySelectorAll('.nav-btn')[map[id]].classList.add('active');
        }

        // ─── Password toggle ────────────────────────────────────────────────────────
        function togglePass(inputId, btn) {
            const inp = document.getElementById(inputId);
            const isPass = inp.type === 'password';
            inp.type = isPass ? 'text' : 'password';
            btn.querySelector('.eye-on').classList.toggle('hidden', isPass);
            btn.querySelector('.eye-off').classList.toggle('hidden', !isPass);
        }

        // ─── Password strength ──────────────────────────────────────────────────────
        function calcStrength(pw) {
            let score = 0;
            if (pw.length >= 8) score++;
            if (/[A-Z]/.test(pw)) score++;
            if (/[0-9]/.test(pw)) score++;
            if (/[^A-Za-z0-9]/.test(pw)) score++;
            return score;
        }

        const STRENGTH_COLORS = ['', '#E24B4A', '#EF9F27', '#1D9E75', '#1D9E75'];
        const STRENGTH_LABELS = ['', 'Weak', 'Medium', 'Strong', 'Very strong'];
        const STRENGTH_TEXT = ['', 'text-danger', 'text-warning', 'text-success', 'text-success'];

        function renderStrength(barId, labelId, pw) {
            const score = pw ? calcStrength(pw) : 0;
            document.querySelectorAll(`#${barId} .strength-seg`).forEach(seg => {
                const i = parseInt(seg.dataset.i);
                seg.style.background = i <= score && score > 0 ? STRENGTH_COLORS[score] : '#e5e7eb';
            });
            const lbl = document.getElementById(labelId);
            lbl.innerHTML = score > 0
                ? `Strength: <strong style="color:${STRENGTH_COLORS[score]}">${STRENGTH_LABELS[score]}</strong>`
                : '';
        }

        function updateStrength(pw) { renderStrength('strength-bar', 'strength-label', pw); }
        function updateStrength2(pw) { renderStrength('strength-bar-2', 'strength-label-2', pw); updateRules(pw); }

        // ─── Password rules ─────────────────────────────────────────────────────────
        const RULES = {
            length: pw => pw.length >= 8,
            upper: pw => /[A-Z]/.test(pw),
            number: pw => /[0-9]/.test(pw),
            special: pw => /[^A-Za-z0-9]/.test(pw),
        };
        function updateRules(pw) {
            document.querySelectorAll('.rule-item').forEach(li => {
                const ok = RULES[li.dataset.rule]?.(pw);
                li.classList.toggle('met', ok);
                li.querySelector('svg').style.color = ok ? '#1D9E75' : '#d1d5db';
            });
        }

        // ─── Confirm password match ─────────────────────────────────────────────────
        function checkConfirm() {
            const pw = document.getElementById('reg-pass').value;
            const conf = document.getElementById('reg-conf').value;
            const ok = pw && conf && pw === conf;
            document.getElementById('conf-ok').classList.toggle('hidden', !ok);
            document.getElementById('conf-err').classList.toggle('hidden', ok || !conf);
            const icon = document.querySelector('#reg-conf').parentElement.querySelector('.ok-icon');
            if (icon) icon.classList.toggle('hidden', !ok);
            setInputState(document.getElementById('reg-conf'), conf ? (ok ? 'success' : 'error') : '');
        }
        function checkConfirm2() {
            const pw = document.getElementById('new-pass').value;
            const conf = document.getElementById('conf-new-pass').value;
            const ok = pw && conf && pw === conf;
            document.getElementById('conf2-ok').classList.toggle('hidden', !ok);
            document.getElementById('conf2-err').classList.toggle('hidden', ok || !conf);
            document.getElementById('conf2-ok-icon').classList.toggle('hidden', !ok);
            setInputState(document.getElementById('conf-new-pass'), conf ? (ok ? 'success' : 'error') : '');
        }

        // ─── OTP wiring ─────────────────────────────────────────────────────────────
        document.querySelectorAll('.otp-box').forEach((box, idx, boxes) => {
            box.addEventListener('input', () => {
                box.value = box.value.replace(/\D/g, '').slice(-1);
                if (box.value && idx < boxes.length - 1) boxes[idx + 1].focus();
                // filled style
                box.style.borderColor = box.value ? '#6C63FF' : '';
                box.style.background = box.value ? '#EEF0FF' : '';
                box.style.color = box.value ? '#6C63FF' : '';
            });
            box.addEventListener('keydown', e => {
                if (e.key === 'Backspace' && !box.value && idx > 0) boxes[idx - 1].focus();
            });
            box.addEventListener('paste', e => {
                e.preventDefault();
                const digits = e.clipboardData.getData('text').replace(/\D/g, '').slice(0, 6);
                boxes.forEach((b, i) => { if (digits[i]) { b.value = digits[i]; b.dispatchEvent(new Event('input')); } });
            });
        });

        // ─── Countdown timer ─────────────────────────────────────────────────────────
        let timerSecs = 42;
        const timerInterval = setInterval(() => {
            const el = document.getElementById('timer-display');
            if (!el) return;
            if (timerSecs > 0) {
                timerSecs--;
                el.textContent = `Resend in 0:${String(timerSecs).padStart(2, '0')}`;
            } else {
                clearInterval(timerInterval);
                document.getElementById('resend-row').innerHTML =
                    `Didn't receive it? <button onclick="handleResend()" class="link cursor-pointer">Resend code</button>`;
            }
        }, 1000);

        // ══════════════════════════════════════════════════════════════════════════
        //  API CALLS — wire these endpoints to your Django REST Framework views
        //  Expected DRF URL patterns (urls.py):
        //
        //  path('api/auth/login/',             views.LoginView.as_view()),
        //  path('api/auth/register/',          views.RegisterView.as_view()),
        //  path('api/auth/forgot-password/',   views.ForgotPasswordView.as_view()),
        //  path('api/auth/reset-password/',    views.ResetPasswordView.as_view()),
        //  path('api/auth/verify-email/',      views.VerifyEmailView.as_view()),
        //  path('api/auth/resend-otp/',        views.ResendOTPView.as_view()),
        // ══════════════════════════════════════════════════════════════════════════

        // ─── Login ──────────────────────────────────────────────────────────────────
        async function handleLogin() {
            hideBanner('login-error');
            const email = document.getElementById('login-email');
            const pass = document.getElementById('login-pass');
            let valid = true;

            if (!email.value || !/\S+@\S+\.\S+/.test(email.value)) {
                setInputState(email, 'error');
                document.getElementById('login-email-err').classList.remove('hidden');
                valid = false;
            } else {
                setInputState(email, '');
                document.getElementById('login-email-err').classList.add('hidden');
            }
            if (!pass.value) {
                setInputState(pass, 'error');
                document.getElementById('login-pass-err').classList.remove('hidden');
                valid = false;
            } else {
                setInputState(pass, '');
                document.getElementById('login-pass-err').classList.add('hidden');
            }
            if (!valid) return;

            setLoading('login-btn', true, 'Signing in...');
            try {
                const { ok, data } = await api('/api/auth/login/', {
                    email: email.value,
                    password: pass.value,
                    remember_me: document.getElementById('remember-me').checked,
                });
                if (ok) {
                    // store token if using JWT (e.g. djangorestframework-simplejwt)
                    if (data.access) localStorage.setItem('access_token', data.access);
                    if (data.refresh) localStorage.setItem('refresh_token', data.refresh);
                    // redirect to dashboard
                    window.location.href = data.redirect || '/dashboard/';
                } else {
                    const msg = data.detail || data.non_field_errors?.[0] || 'Invalid email or password.';
                    showBanner('login-error', 'login-error-msg', msg);
                    setInputState(email, 'error');
                    setInputState(pass, 'error');
                }
            } catch (err) {
                showBanner('login-error', 'login-error-msg', 'Network error. Please try again.');
            } finally {
                setLoading('login-btn', false);
            }
        }

        // ─── Register ───────────────────────────────────────────────────────────────
        async function handleRegister() {
            hideBanner('register-error');
            const name = document.getElementById('reg-name');
            const username = document.getElementById('reg-username');
            const email = document.getElementById('reg-email');
            const pass = document.getElementById('reg-pass');
            const conf = document.getElementById('reg-conf');
            const terms = document.getElementById('reg-terms');

            let valid = true;
            if (!name.value.trim()) { setInputState(name, 'error'); valid = false; } else setInputState(name, 'success');
            if (!username.value.trim()) { setInputState(username, 'error'); valid = false; }
            if (!/\S+@\S+\.\S+/.test(email.value)) { setInputState(email, 'error'); valid = false; } else setInputState(email, 'success');
            if (calcStrength(pass.value) < 2) { setInputState(pass, 'error'); valid = false; }
            if (pass.value !== conf.value || !conf.value) { setInputState(conf, 'error'); valid = false; }
            if (!terms.checked) {
                showBanner('register-error', 'register-error-msg', 'Please accept the Terms of Service.');
                valid = false;
            }
            if (!valid) return;

            setLoading('register-btn', true, 'Creating account...');
            try {
                const { ok, data } = await api('/api/auth/register/', {
                    full_name: name.value.trim(),
                    username: username.value.trim(),
                    email: email.value,
                    password: pass.value,
                    password2: conf.value,
                });
                if (ok) {
                    // store pending email for verify screen
                    document.getElementById('verify-email-display').textContent = email.value;
                    show('verify');
                } else {
                    const msg = data.detail || Object.values(data).flat()[0] || 'Registration failed.';
                    showBanner('register-error', 'register-error-msg', msg);
                }
            } catch (err) {
                showBanner('register-error', 'register-error-msg', 'Network error. Please try again.');
            } finally {
                setLoading('register-btn', false);
            }
        }

        // ─── Forgot password ────────────────────────────────────────────────────────
        async function handleForgot() {
            const emailInp = document.getElementById('forgot-email');
            const errEl = document.getElementById('forgot-email-err');
            if (!emailInp.value || !/\S+@\S+\.\S+/.test(emailInp.value)) {
                setInputState(emailInp, 'error');
                errEl.classList.remove('hidden');
                return;
            }
            setInputState(emailInp, '');
            errEl.classList.add('hidden');

            setLoading('forgot-btn', true, 'Sending...');
            try {
                const { ok, data } = await api('/api/auth/forgot-password/', { email: emailInp.value });
                if (ok) {
                    document.getElementById('sent-to').textContent = emailInp.value;
                    document.getElementById('forgot-form').classList.add('hidden');
                    document.getElementById('forgot-success').classList.remove('hidden');
                } else {
                    setInputState(emailInp, 'error');
                    errEl.textContent = data.detail || 'Could not send reset link.';
                    errEl.classList.remove('hidden');
                }
            } catch {
                errEl.textContent = 'Network error. Please try again.';
                errEl.classList.remove('hidden');
            } finally {
                setLoading('forgot-btn', false);
            }
        }

        // ─── Reset password ─────────────────────────────────────────────────────────
        async function handleReset() {
            const newPass = document.getElementById('new-pass');
            const confPass = document.getElementById('conf-new-pass');
            const token = document.getElementById('reset-token').value;
            const uid = document.getElementById('reset-uid').value;

            if (calcStrength(newPass.value) < 2) { setInputState(newPass, 'error'); return; }
            if (newPass.value !== confPass.value) { setInputState(confPass, 'error'); return; }

            setLoading('reset-btn', true, 'Resetting...');
            try {
                const { ok, data } = await api('/api/auth/reset-password/', {
                    uid,
                    token,
                    new_password: newPass.value,
                    new_password2: confPass.value,
                });
                if (ok) {
                    // password reset success — go to login with a toast
                    show('login');
                    showBanner('login-error', 'login-error-msg', ''); // reuse banner as success — or add a success banner
                    // quick inline toast
                    const toast = document.createElement('div');
                    toast.className = 'fixed top-4 right-4 bg-green-600 text-white text-sm px-4 py-3 rounded-xl shadow-lg z-50 flex items-center gap-2';
                    toast.innerHTML = `<svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="9 12 11 14 15 10"/></svg> Password reset! Please sign in.`;
                    document.body.appendChild(toast);
                    setTimeout(() => toast.remove(), 4000);
                } else {
                    const msg = data.detail || 'Reset failed. The link may have expired.';
                    alert(msg); // replace with a proper error banner if desired
                }
            } catch {
                alert('Network error. Please try again.');
            } finally {
                setLoading('reset-btn', false);
            }
        }

        // ─── Verify email (OTP) ─────────────────────────────────────────────────────
        async function handleVerify() {
            hideBanner('verify-error');
            const boxes = document.querySelectorAll('.otp-box');
            const code = [...boxes].map(b => b.value).join('');
            if (code.length < 6) {
                showBanner('verify-error', 'verify-error-msg', 'Please enter the full 6-digit code.');
                return;
            }

            setLoading('verify-btn', true, 'Verifying...');
            try {
                const email = document.getElementById('verify-email-display').textContent;
                const { ok, data } = await api('/api/auth/verify-email/', { email, code });
                if (ok) {
                    if (data.access) localStorage.setItem('access_token', data.access);
                    if (data.refresh) localStorage.setItem('refresh_token', data.refresh);
                    document.getElementById('success-name').textContent = data.first_name || email.split('@')[0];
                    show('success');
                } else {
                    showBanner('verify-error', 'verify-error-msg', data.detail || 'Invalid or expired code.');
                    boxes.forEach(b => { b.style.borderColor = '#E24B4A'; b.style.background = ''; b.style.color = ''; });
                }
            } catch {
                showBanner('verify-error', 'verify-error-msg', 'Network error. Please try again.');
            } finally {
                setLoading('verify-btn', false);
            }
        }

        // ─── Resend OTP ─────────────────────────────────────────────────────────────
        async function handleResend() {
            const email = document.getElementById('verify-email-display').textContent;
            try {
                await api('/api/auth/resend-otp/', { email });
                // restart timer
                timerSecs = 42;
                document.getElementById('resend-row').innerHTML =
                    `Didn't receive it? <span id="timer-display" class="text-primary font-medium">Resend in 0:42</span>`;
            } catch {
                alert('Could not resend. Please try again.');
            }
        }

        // ─── Dashboard redirect ──────────────────────────────────────────────────────
        function handleDashboard() {
            setLoading('dashboard-btn', true, 'Opening dashboard...');
            setTimeout(() => { window.location.href = '/dashboard/'; }, 800);
        }