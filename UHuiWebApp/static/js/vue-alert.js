 var vueconfirm = new Vue({
        el: '#V-confirm',
        data: {
            show: false,
            onCancel: false,
            onOk: false,
            title: '',
            content: '',
            button1: '',
            button2: ''
        },
        methods: {
            op: function (type) {
                this.show = false;
                if (type === 'cancel') {
                    if (this.onCancel) this.onCancel()
                }
                else {
                    if (this.onOk) this.onOk()
                }

                this.onCancel = false;
                this.onOk = false;

                document.body.style.overflow = '';
            },
            alert: function (setting) {
                this.title = setting.title || '';
                this.content = setting.content || '';
                this.button1 = setting.button1 || '取 消';
                this.button2 = setting.button2 || '确 定';
                this.onOk = setting.onOk || false;
                this.onCancel = setting.onCancel || false;
                this.show = true;
                document.body.style.overflow = 'hidden';
            }
        }
    });
    var vuealert = new Vue({
        el: '#V-alert',
        data: {
            show: false,
            onOk: false,
            title: '',
            content: '',
            button: ''
        },
        methods: {
            op: function () {
                this.show = false;
                if (this.onOk) this.onOk();

                this.onCancel = false;
                this.onOk = false;

                document.body.style.overflow = '';
            },
            alert: function (setting) {
                this.title = setting.title || '';
                this.content = setting.content || '';
                this.button = setting.button || '确 定';
                this.onOk = setting.onOk || false;
                this.show = true;
                document.body.style.overflow = 'hidden';
            }
        }
    });
    var vueinput = new Vue({
        el: '#V-input',
        data: {
            show: false,
            onCancel: false,
            onOk: false,
            title: '',
            content: '',
            button1: '',
            button2: '',
            message: ''
        },
        methods: {
            op: function (type) {
                this.show = false;
                if (type === 'cancel') {
                    if (this.onCancel) this.onCancel()
                }
                else {
                    if (this.onOk) this.onOk()
                }

                this.onCancel = false;
                this.onOk = false;

                document.body.style.overflow = '';
                this.message = '';
            },
            alert: function (setting) {
                this.title = setting.title || '';
                this.content = setting.content || '';
                this.button1 = setting.button1 || '取 消';
                this.button2 = setting.button2 || '确 定';
                this.onOk = setting.onOk || false;
                this.onCancel = setting.onCancel || false;
                this.show = true;
                document.body.style.overflow = 'hidden';
            }
        }
    });